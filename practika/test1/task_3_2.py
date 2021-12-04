print('Веедите ip-адрес и маску (a.a.a.a/b):', end='')
ip = input().split(".")
mask =  int(ip[-1].strip().split('/')[1])
print(mask)
print("Network: ")
print(ip[0], end = " " * (12 - len(ip[0])))
print(ip[1], end = " " * (12 - len(ip[1])))
print(ip[2], end = " " * (12 - len(ip[2])))
print(ip[3].strip().split('/')[0], end = " " * (12 - len(ip[3])))
print()
a1 = bin(int(ip[0]))
a2 = bin(int(ip[1]))
a3 = bin(int(ip[2]))
a4 = bin(int(ip[-1].strip().split('/')[0]))
print(a1[2::].zfill(8), a2[2::].zfill(8), a3[2::].zfill(8), a4[2::].zfill(8), sep = " " * 4)

mask_out = mask*'1' + (32-mask)*'0'
mask1, mask2, mask3, mask4 = [mask_out[0:8], mask_out[8:16], mask_out[16:24], mask_out[24:32]]
mask1_10, mask2_10, mask3_10, mask4_10 = [int(mask_out[0:8], 2), int(mask_out[8:16], 2), int(mask_out[16:24], 2), int(mask_out[24:32], 2)]

out_mask_10 = '{:<10}{:<10}{:<10}{:<10}'
out_mask_2 = '{:10}{:10}{:10}{:10}'

print('Mask: ', '/', mask, sep=" ")
print(out_mask_10.format(mask1_10, mask2_10, mask3_10, mask4_10))
print(out_mask_2.format(mask1, mask2, mask3, mask4))
