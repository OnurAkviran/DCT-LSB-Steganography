import math

# 8x8 pixel block m,n represents x,y
m = 8
n = 8
PI = math.pi

# 2nd DCT function is used in embedding data
def DCT_II(matrix):

    dct = []

    for i in range(m):
        dct.append([None for _ in range(n)])

    for i in range(m):
        for j in range(n):

            #ci and cj according to the matrix form
            #of the equation. (Tij)

            if (i == 0):
                ci = 1 / (math.sqrt(m))
            else:
                ci = math.sqrt(2/m)
            
            if (j == 0):
                cj = 1 / (math.sqrt(n))
            else:
                cj = math.sqrt(2/n)

            #sum of cosine values
            cos_sum = 0
            for k in range(m):
                for l in range(n):

                    dct1 =  matrix[k][l] * math.cos((2 * k + 1) * i * PI / (
                        2 * m)) * math.cos((2 * l + 1) * j * PI / (2 * n))

                    cos_sum = cos_sum + dct1
                    dct[i][j] = ( 1  / math.sqrt( 2 * n )) * ci * cj * cos_sum
      
    for i in range(m):
        for j in range(n):
            print(dct[i][j], end="\t")
        print()
        

 
