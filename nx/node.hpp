#ifndef NX_NODE_INC
#define NX_NODE_INC

#include <vector>
#include <algorithm>
#include "indexable.hpp"

namespace nx {

template <typename N,
          typename Ix=DefaultIx>
class Node : public NodeIndex<Ix>
{
public:
    Node(Ix ix, N w);
    
    std::vector<EdgeIndex<Ix>*> neighbor_edges(Direction dir=nx::NONE) const;
    
    void island();
    
    void connect(EdgeIndex<Ix>* eix, Direction dir);
    void disconnect(EdgeIndex<Ix>* eix, Direction dir);
    
    inline N& payload() {
        return this->weight_;
    }
    
private:
    N weight_;
    std::vector<EdgeIndex<Ix>*> edges_i_;
    std::vector<EdgeIndex<Ix>*> edges_o_;
};
  
} // namespace nx

#endif // NX_NODE_INC
