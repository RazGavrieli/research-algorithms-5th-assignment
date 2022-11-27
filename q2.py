def c(name, *nums):
    def add(nums):
        s=0
        for i in nums:
            s+=i
        return s
    def mul(nums):
        s=1
        for i in nums:
            s*=i
        return s
    dict = {'add': add, 'mul': mul}
    return dict[name](nums)

print(c('add', 1,2,5))
print(c('mul', 1,2,5))

