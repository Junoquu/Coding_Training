e_t,e_f,e_s,e_p,e_c=map(int,input().split())
h_t,h_f,h_s,h_p,h_c=map(int,input().split())

e=6*e_t+3*e_f+2*e_s+e_p+2*e_c
h=6*h_t+3*h_f+2*h_s+h_p+2*h_c

print(e,h)