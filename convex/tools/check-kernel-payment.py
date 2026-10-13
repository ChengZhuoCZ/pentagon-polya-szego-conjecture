from fractions import Fraction as F
import json
T=F(27,50);r=F(619,1000);bm=F(63,100);xmax=bm*bm
checks={};rows=[]
def check(n,c):
 assert c,n
 checks[n]=True
for name,k,cap,df,dh,m in [('U',F(1),F(5,8),F(1,750),F(1,1000),F(435,1000)),('C',F(6,5),T,F(1,250),F(1,400),F(241,500))]:
 raw=k**6*(11+(11+9*r)*T+(11*r+9)*cap)/2000
 check(name+'_full_alias_f',raw*T**4<df)
 check(name+'_full_alias_h',raw*T**5<dh)
 check(name+'_F_greater_J',1+(1-r)*(0-cap)>0)
 check(name+'_positive_coefficient',1-F(4,5)*k*cap>0)
 if name=='U':check('U_mean_rectangle',F('.144')*T+F('.570')*cap<m)
 else:check('C_mean_triangle',F('.891')*T<m)
 for ep,lo0,lo2,hi0,hi2 in [(-1,F('2.380'),F('2.570'),F('2.381'),F('2.290')),(1,F('1.542'),F('.207'),F('1.543'),F('.189'))]:
  X=F('.3947') if ep==1 else F('.3948')
  fc=k*k*(F(1,2)+ep*X/6-k*k*T*T/12)-k**5*T**3/200-k**4*T**3/32+k*(1-F(4,5)*k*cap)*(lo0-k*k*T*T/7)-df
  f2=k*k*ep/6+k*(1-F(4,5)*k*cap)*lo2
  hc=k*k*T/2+k*(F(4,5)*k*T*T+cap)*(hi0+k*k*T*T/7)+cap*k**4*T**3/32+dh
  h2=k*(F(4,5)*k*T*T+cap)*hi2
  f0=F((fc*1000).__floor__(),1000);f2c=F((f2*1000).__ceil__(),1000);A=F((hc*1000).__ceil__(),1000);B=F((h2*1000).__floor__(),1000)
  key=f'{name}_{ep}'
  check(key+'_F0',f0<=fc);check(key+'_F2',f2<=f2c);check(key+'_H0',hc<=A);check(key+'_H2',B<=h2)
  check(key+'_F_at_endpoint',f0-f2c*xmax>1)
  check(key+'_H_nonnegative',A-B*xmax>0)
  check(key+'_radial_positive',lo0-lo2*xmax-k*k*T*T/7>0)
  linear=min(f0-m*A, f0-m*A+(-f2c+m*B)*xmax)
  if ep==-1:
   pay=F('.330') if name=='U' else F('.470')
   check(key+'_quintic_max_square',F(256,3125)*A**5/B<(F(16,3)*pay)**2)
  else:
   check(key+'_quintic_increasing',A-5*B*xmax>0)
   pay=F(3,16)*bm*(A-B*xmax)**2
  margin=linear-pay
  check(key+'_E_positive',margin>F(1,100))
  rows.append({'branch':name,'epsilon':ep,'F0':str(f0),'F2':str(f2c),'H0':str(A),'H2':str(B),'F_min':str(f0-f2c*xmax),'E_margin':str(margin),'E_margin_decimal':float(margin),'quintic_payment_upper':str(pay)})
check('mass_tan_bound',5-2*F(559,250)<F(9,16))
print(json.dumps({'all_pass':True,'count':len(checks),'checks':checks,'rows':rows,'scope':'Exact finite constants for full kernel rectangle/triangle and finite-mass payment; continuous steps are in QMD.'},indent=2))
