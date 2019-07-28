# def trap(height):
#     _sum = 0
#     if len(height)<3 :
#         return 0
#     for i in range(1,len(height)-1):
#         left_max = 0
#         right_max = 0
#         for j in range(i+1):
#             left_max = max(left_max,height[j])
#         for k in range(i,len(height)):
#             right_max = max(right_max,height[k])
#         _sum += min(left_max,right_max)-height[i]
#
#     return _sum
#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         _sum = 0
#         if len(height)<3 :
#             return 0
#         for i in range(1,len(height)-1):
#             left_max = max(height[0:i])
#             right_max = max(height[i+1:])
#             x = min(left_max,right_max)-height[i]
#             if x > 0:
#                 _sum += x
#         return _sum
#
#
#
#
#
# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

def deepCopy(src):
    if isinstance(src, dict):
        dst = {}
        for k, v in src.items():
            dst[k] = deepCopy(v)
        return dst

    elif isinstance(src, (list,tuple)):
        dst = []
        for i in src:
            dst.append(deepCopy(i))
        if isinstance(src,list):
            return dst
        else:
            return tuple(dst)
    else:
        return src


if __name__ == '__main__':
    numlist = ([1, 2, {3, 4, 5}], 34, "abc", {"name": {"fistname": "王", "lastName": "二", "listname": [1, 2, 3]}},)

print(numlist)
print(type(numlist))
out = deepCopy(numlist)
out[0][2] = {3,4,6}
print(out)
print(numlist)

#你好，复制了你的代码，在python3中运行，tuple类型并不会满足elif中的条件，改成elif isinstance（src，（list，tuple））貌似可以了，
# 还有就是此段代码中会将tuple格式数据转换成list，建议返回时再加个判断
