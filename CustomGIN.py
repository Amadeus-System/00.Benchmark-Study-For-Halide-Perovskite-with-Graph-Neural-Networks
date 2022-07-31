class CustomGIN(torch.nn.Module):

    def __init__(self, in_channels = 92, hidden_channels = 16, num_layers = 3, out_channels = 1, dropout: float = 0.2):
        super().__init__()
        self.name = 'GIN_Baseline'
        self.in_channels = in_channels
        self.hidden_channels = hidden_channels
        self.num_layers = num_layers
        self.out_channels = out_channels
        self.dropout = dropout
        self.convs = torch.nn.ModuleList()
        self.batch_norms = torch.nn.ModuleList()

        for i in range(self.num_layers):
            mlp = Sequential(Linear(in_channels, 2 * hidden_channels), BatchNorm(2 * hidden_channels),
                             ReLU(), Linear(2 * hidden_channels, in_channels)) # Callable nn
            conv = CustomGINConv(nn = mlp, eps = 0.1, train_eps = True)
            self.convs.append(conv)
            self.batch_norms.append(BatchNorm(in_channels))
        
        self.lin = Linear(self.in_channels, self.hidden_channels)
        self.batch_norm = BatchNorm(self.hidden_channels)
        self.regression = Linear(self.hidden_channels, 1)

    def forward(self, sample):
        x, edge_index, edge_attr, batch = sample.x, sample.edge_index, sample.edge_attr, sample.batch

        for conv, batch_norm in zip(self.convs, self.batch_norms): # convolution 및 BN 연달아 적용
            x = F.relu(batch_norm(conv(x, edge_index, edge_attr)))
        
        h = x.clone().detach()  # Node Embedding
        x = global_add_pool(x, batch)
        x = F.relu(self.batch_norm(self.lin(x)))
        x = F.dropout(x, p = self.dropout, training = self.training)
        out = self.regression(x)
        out = out.view(-1)      # 배치차원 맞추기 위해
        return out, h 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = CustomGIN().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001, weight_decay = 5e-4)
criterion = torch.nn.MSELoss()
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer = optimizer, mode = 'min', patience = 3, verbose = True)
sample = sample.to(device)
out, _ = model(sample)

print(out.shape, sample.y.shape, '\n')
assert out.shape == sample.y.shape, 'out.shape must be equal to sample.y.shape!!' 
print('Model : {}'.format(model))
print('Optimizer : {}'.format(optimizer))
print('Criterion : {}'.format(criterion))
print('Scheduler : {}'.format(scheduler))
