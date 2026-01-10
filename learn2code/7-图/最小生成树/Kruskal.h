template <class ElemType, class WeightType>
class KruskalEdge
{
public:
    ElemType vertex1, vertex2;
    WeightType weight;
    KruskalEdge(ElemType v1, ElemType v2, WeightType w);
    KruskalEdge() {};
    KruskalEdge<ElemType, WeightType> &operator=(
        const KruskalEdge<ElemType, WeightType> &Ed);
    bool operator<=(const KruskalEdge<ElemType,
                                      WeightType> &Ed) const;
    bool operator>(const KruskalEdge<ElemType,
                                     WeightType> &Ed) const;
};
