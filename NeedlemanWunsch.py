gap = -6
m=0
n=0
c=0
LastScore = []
# Score matrix array = "[AA, AT, AC, AG, TT, TC, TG, CC, CG, GG]"
ScoreMatrixArray = [    [5,-1,-4,-4,8,-3,-4,4,-4,6], [1,0,0,0,1,0,0,1,0,1], 
                        [5,-4,-4,-4,5,-4,-4,5,-4,5], [0,5,5,1,0,1,5,0,5,0] ]



seq1 = '-ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTC'
#seq1 =     '-ATGGCAA' 
#seq2array=['-ATCGCGA']
seq2array = ['-TTGTAGATCTGTTATTAAAGGTTTTAAAATCTGTGTGGCTGTCACTCCTC',
            '-TTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTC',
            '-GGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGT',
            '-CGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGT',
            '-TTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTG',
            '-ATTAGGGGTTTATATCTTCCCAGGTACCAAACCCACCAACTTTCGATCTC',
            '-TTCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACCGTCCGGGTG',
            '-TGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAAC',
            '-ACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTAC',
            '-GTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACAT',
            '-CTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCC',
            '-ATTAAAGGTTTATACTGTGGCTTAGTAGAAGTTAACCAACTTTCGATCTC',
            '-CTTATTGATAACACTTGTTTCTTAGAAAAAGTTGAAAAAGGCGTTAAGCC',
            '-TCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTG',
            '-CACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATT',
            '-CAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGG',
            '-CGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATA',
            '-AAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTA',
            '-AACCCGCTGGTGGCCATAGTTAGATTACCCGGCTAAAGTCATTTGACTTA',
            '-GGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAA',
            '-CACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGGGGTTTCTTAACG',
            '-ACACCTCATGTCCGAACAACTGGACGAGGGGGACACTAAGAGGGGTGTAT',
            '-GATATACCTTACACTCGCTATGTCGATAACAACTTCTGTGGCCCTGATGG',
            '-TACCCTCTTGAGTGCATTAAAGACCTTCTAGCACGTGCTGGTAAAGCTTC',
            '-ATGCACTTTGTCCGAACAACTGGACTTTATTGACACTAAGAGGGGTGTAT',
            '-ATTAAATTTGTCCGAACAACTGGACTTTATTGACACTAAGAGTATATGGC']



for t in range(len(seq2array)):
    seq2 = seq2array[t]
    out1=[] # i
    out2=[] # j
    for v in range(len(ScoreMatrixArray)):
        
        ScoreMatrixPoint = 0
        AAeslesmesi = ScoreMatrixArray[v][0]
        ATeslesmesi = ScoreMatrixArray[v][1]
        ACeslesmesi = ScoreMatrixArray[v][2]
        AGeslesmesi = ScoreMatrixArray[v][3]
        TTeslesmesi = ScoreMatrixArray[v][4]
        TCeslesmesi = ScoreMatrixArray[v][5]
        TGeslesmesi = ScoreMatrixArray[v][6]
        CCeslesmesi = ScoreMatrixArray[v][7]
        CGeslesmesi = ScoreMatrixArray[v][8]
        GGeslesmesi = ScoreMatrixArray[v][9]    
        
        c=0
        board = [ [0 for i in range(len(seq2))] for j in range(len(seq1))]

        for i in range(len(seq1)):
            if(i==1):
                c = -6
            for j in range(len(seq2)):
                selected = 0
                if(j<1 or i<1):
                    board[i][j] = c
                    c = c - 6
                if(i>=1 and j>=1):
                    
                    if(seq1[i] == 'A' and seq2[j] == 'A'):
                        selected = AAeslesmesi 
                        
                    if(seq1[i] == 'A' and seq2[j] == 'T'):
                        selected = ATeslesmesi 
                    if(seq1[i] == 'T' and seq2[j] == 'A'):
                        selected = ATeslesmesi 
                        
                    if(seq1[i] == 'A' and seq2[j] == 'C'):
                        selected = ACeslesmesi 
                    if(seq1[i] == 'C' and seq2[j] == 'A'):
                        selected = ACeslesmesi    
                        
                    if(seq1[i] == 'A' and seq2[j] == 'G'):
                        selected = AGeslesmesi 
                    if(seq1[i] == 'G' and seq2[j] == 'A'):
                        selected = AGeslesmesi 
                        
                    if(seq1[i] == 'T' and seq2[j] == 'T'):
                        selected = TTeslesmesi 
                        
                    if(seq1[i] == 'T' and seq2[j] == 'C'):
                        selected = TCeslesmesi 
                    if(seq1[i] == 'C' and seq2[j] == 'T'):
                        selected = TCeslesmesi            
                        
                    if(seq1[i] == 'T' and seq2[j] == 'G'):
                        selected = TGeslesmesi 
                    if(seq1[i] == 'G' and seq2[j] == 'T'):
                        selected = TGeslesmesi  
                        
                    if(seq1[i] == 'C' and seq2[j] == 'C'):
                        selected = CCeslesmesi 
                        
                    if(seq1[i] == 'C' and seq2[j] == 'G'):
                        selected = CGeslesmesi 
                    if(seq1[i] == 'G' and seq2[j] == 'C'):
                        selected = CGeslesmesi 
                        
                    if(seq1[i] == 'G' and seq2[j] == 'G'):
                        selected = GGeslesmesi
                        
                    MaxDeger = max(board[i][j-1] + gap, board[i-1][j] + gap, board[i-1][j-1] + selected)
                    board[i][j] = MaxDeger
                        
        for line in board:
            print(line)     
            
        print("\n")
        
        #backtracking
        q = len(seq1)-1
        w = len(seq2)-1

            #   seq1 dikey i,q ---  seq2 yatay  j,w
        while(1):

            if(q>0 and w>0):
                if(board[q][w-1] > board[q-1][w] or board[q][w-1] == board[q-1][w]):  
                    if(board[q][w-1] > board[q-1][w-1]):
                        w = w-1
                        out1.append("-")
                        out2.append(seq2[w])
                    else:
                        w = w-1
                        q = q-1
                        out1.append(seq1[q])
                        out2.append(seq2[w])
                else:
                    if(board[q-1][w] > board[q-1][w-1]):
                        q = q-1
                        out2.append("-")
                        out1.append(seq1[q])
                    else:
                        w = w-1
                        q = q-1
                        out1.append(seq1[q])
                        out2.append(seq2[w])              
            if(q>0 and w==0):
                q = q-1
                out2.append("-")
                out1.append(seq1[q])
               
            if(w>0 and q==0):
                w = w-1
                out1.append("-")
                out2.append(seq2[w])      
               
            if(q==0 and w==0):
                break
            
        out1.reverse()
        out2.reverse()

        
        for i in range(len(out1)):
             if(out1[i] == '-' or out2[i] == '-' ):
                ScoreMatrixPoint = ScoreMatrixPoint - 6 
             if(out1[i] == 'A' and out2[i] == 'A' ):
                ScoreMatrixPoint = ScoreMatrixPoint + AAeslesmesi  
                
             if(out1[i] == 'A' and out2[i] == 'T' ):
                ScoreMatrixPoint = ScoreMatrixPoint + ATeslesmesi   
             if(out1[i] == 'T' and out2[i] == 'A' ):
                ScoreMatrixPoint = ScoreMatrixPoint + ATeslesmesi
                
             if(out1[i] == 'A' and out2[i] == 'C' ):
                ScoreMatrixPoint = ScoreMatrixPoint + ACeslesmesi   
             if(out1[i] == 'C' and out2[i] == 'A' ):
                ScoreMatrixPoint = ScoreMatrixPoint + ACeslesmesi 
                
             if(out1[i] == 'A' and out2[i] == 'G' ):
                ScoreMatrixPoint = ScoreMatrixPoint + AGeslesmesi  
             if(out1[i] == 'G' and out2[i] == 'A' ):
                ScoreMatrixPoint = ScoreMatrixPoint + AGeslesmesi  
                
             if(out1[i] == 'T' and out2[i] == 'T' ):
                ScoreMatrixPoint = ScoreMatrixPoint + TTeslesmesi   
                
             if(out1[i] == 'T' and out2[i] == 'C' ):
                ScoreMatrixPoint = ScoreMatrixPoint + TCeslesmesi   
             if(out1[i] == 'C' and out2[i] == 'T' ):
                ScoreMatrixPoint = ScoreMatrixPoint + TCeslesmesi  
                
             if(out1[i] == 'T' and out2[i] == 'G' ):
                ScoreMatrixPoint = ScoreMatrixPoint + TGeslesmesi   
             if(out1[i] == 'G' and out2[i] == 'T' ):
                ScoreMatrixPoint = ScoreMatrixPoint + TGeslesmesi 
                
             if(out1[i] == 'C' and out2[i] == 'C' ):
                ScoreMatrixPoint = ScoreMatrixPoint + CCeslesmesi  
                
             if(out1[i] == 'C' and out2[i] == 'G' ):
                ScoreMatrixPoint = ScoreMatrixPoint + CGeslesmesi
             if(out1[i] == 'G' and out2[i] == 'C' ):
                ScoreMatrixPoint = ScoreMatrixPoint + CGeslesmesi  
                
             if(out1[i] == 'G' and out2[i] == 'G' ):
                ScoreMatrixPoint = ScoreMatrixPoint + GGeslesmesi             
        LastScore.append([''.join(out1),''.join(out2),ScoreMatrixPoint,ScoreMatrixArray[v]])
    
    
    
print("\n")
maks=int(LastScore[0][2])
EnBuyukItem = LastScore[0]


for i in range(len(LastScore)):
    if(int(LastScore[i][2]) > maks):
        maks = LastScore[i][2]
        EnBuyukItem = LastScore[i]
        


print("En Buyuk Deger:")
print(EnBuyukItem[0])
print("\n")
print(EnBuyukItem[1])
print("\n")
print("SCORE")
print(EnBuyukItem[2])
print("Matris")
print(EnBuyukItem[3])

