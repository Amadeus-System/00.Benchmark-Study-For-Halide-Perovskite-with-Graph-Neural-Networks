class CustomGINConv(MessagePassing):

    def __init__(self, nn: Callable, eps: float = 0.1, train_eps: bool = True, **kwargs):
        kwargs.setdefault('aggr', 'add')    # self.aggr = 'add' 설정인듯
        super().__init__(**kwargs)
        self.nn = nn  # Differential Parametric Function
        self.initial_eps = eps
        self.message_embedding = torch.nn.Linear(92 + edge_attr_dim, 92) # 도메인 적용을 위한 변환층
        if train_eps:
            self.eps = torch.nn.Parameter(torch.Tensor([eps]))  # epsilon을 trainable parameter로 설정
        else:
            self.register_buffer('eps', torch.Tensor([eps]))    # 부차적인 버퍼? 
        self.reset_parameters()

    def reset_parameters(self):
        reset(self.nn) 
        self.eps.data.fill_(self.initial_eps)   # initial eps를 초기 eps로 설정
    
    def forward(self, x: Union[Tensor, OptPairTensor], edge_index: Adj, edge_attr, size: Size = None) -> Tensor:
        if isinstance(x, Tensor):
            x: OptPairTensor = (x, x)
        
        # 메시지 전파
        out = self.propagate(edge_index, x = x, edge_attr = edge_attr, size = size)

        x_r = x[1]  # 복사된 정보
        if x_r is not None:
            assert out.shape == x_r.shape
            out += (1 + self.eps) * x_r  # x : 원래 노드 정보를 (1 + eps) 가중치 주고, 업데이트된 노드 정보와 비율적으로 결합.
        return self.nn(out)              # 임의의 뉴럴 네트워크에 통과

    def message(self, x_i: Tensor, x_j: Tensor, edge_attr) -> Tensor:
        cgcnn_z = torch.cat([x_j, edge_attr], dim = -1) # 여기서는 x_i 의도적으로 안넣었음!
        out = self.message_embedding(cgcnn_z) # 차원 조정
        return out

    def message_and_aggregate(self, adj_t: SparseTensor, x: OptPairTensor) -> Tensor:
        print('message and aggregate 의도치 않은 발동!!')
        adj_t = adj_t.set_value(None, layout = None)
        return matmul(adj_t, x[0], reduce = self.aggr)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(nn = {self.nn})'

mlp = Sequential(Linear(92, 16), BatchNorm(16), ReLU(), Linear(16, 92))    # 여기서 GINConv에 들어가는 nn은 input/output 차원 같아야 편함
sample = sample.to(device)
ginconv = CustomGINConv(nn = mlp, eps = 0.1, train_eps = True).to(device)
print(ginconv(sample.x, sample.edge_index, sample.edge_attr).shape)
