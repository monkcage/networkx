#ifndef NX_INDEXABLE_INC
#define NX_INDEXABLE_INC

#include <limits>
#include <memory>
#include <cinttypes>
#include <type_traits>

namespace gx {

enum Direction : uint8_t {
    INCOMING = 1 << 0,
    OUTGOING = 1 << 1,
    NONE     = INCOMING | OUTGOING
};
 
using DefaultIx = uint16_t;
  
template <typename Ix>
class Indexable
{
    static_assert(std::is_integer<Ix>::value != 0,
                  "Ix must be integer type.");
    static_assert(std::numeric_limits<Ix>::min() >= 0,
                  "std::numeric_limits<Ix>::min() must be non-negative");
 
public:
    Indexable(Ix ix)
        : ix_(std::move(ix))
    {}
  
    virtual ~Indexable() = default;
  
    inline Ix index() const {
        return ix_;
    }
  
protected:
    Ix ix_;
};
  
  
template <typename Ix=DefaultIx>
class NodeIndex : public Indexable<Ix>
{
public:
    NodeIndex(Ix ix)
        : Indexable<Ix>(std::move(ix))
    {}
    
    virtual ~NodeIndex() {}
    
    inline bool operator==(NodeIndex const& rhs) const {
        return this->ix_ == rhs.ix_;
    }
    
    inline bool operator<(NodeIndex const& rhs) const {
        return this->ix_ < rhs.ix_;
    }
    
    inline bool operator==(Ix const& ix) const {
        return this->ix_ == ix;
    }
    
    inline bool operator<(Ix const& ix) const {
        return this->ix_ < ix;
    }
};
  

template <typename Ix=DefaultIx>
class EdgeIndex : public Indexable<Ix>
{
public:
    EdgeIndex(Ix ix)
        : Indexable<Ix>(std::move(ix))
    {}
    
    virtual ~EdgeIndex() {}
    
    inline bool operator==(EdgeIndex const& rhs) const {
        return this->ix_ == rhs.ix_;
    }
    
    inline bool operator<(EdgeIndex const& rhs) const {
        return this->ix_ < rhs.ix_;
    }
    
    inline bool operator==(Ix const& xi) const {
        return this->ix_ == ix;
    }
    
    inline bool operator<(Ix const& ix) const {
        return this->ix_ < ix;
    }
};
  
} // namespace gx

#endif // NX_INDEXABLE_INC
