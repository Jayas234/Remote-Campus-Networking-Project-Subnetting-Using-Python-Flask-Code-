from flask import *

app=Flask(__name__)

@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
	if request.method=="POST":
		ips=int(request.form['ip'])
		results=[]
		defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
		subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
		k=1
		while True:
		    c=2**k
		    if c>=ips:
		            break
		    else:
		        k+=1
		if c<255:
		    l=defaultsubnet[2]
		    def_sub=defaultsubnet[2]
		elif c<65025:
		    l=defaultsubnet[1]
		    def_sub=defaultsubnet[1]
		elif c<16581375:
		    l=defaultsubnet[0]
		    def_sub=defaultsubnet[0]
		e=(32-k)*"1"
		f=k*'0'
		g=e+f
		i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
		j=subnet[l]
		bin_rep=g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::])
		h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
		new_sub='.'.join(h)
		prefix_len=i.count('1')
		z=i.count('1')-j.count('1')
		networks=int(2**(z))
		hosts=c
		#print(bin_rep,new_sub,prefix_len,networks,hosts)
		#return redirect(url_for('home'))
		#return render_template("home.html",def_sub=def_sub,bin_rep=bin_rep,new_sub=new_sub,prefix_len=prefix_len,networks=networks,hosts=hosts)
		data=[def_sub,bin_rep,new_sub,prefix_len,networks,hosts]
		results.append(data)
		return render_template("home.html",results=results)
	return render_template("home.html")
@app.route("/about",methods=["GET","POST"])
def about():
	if request.method=="POST":
		#Method=request.form['Enter the Required IP']
		ips=request.form['ip']
		ips=ips.split()
		results=[]
		for i in range(len(ips)):
			k=1
			#print("The Details of",ips[i],"Hosts are:")
			a=0
			a=int(ips[i])
			defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
			subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
			k=1
			while True:
				c=2**k
				if c>=int(ips[i]):
					break
				else:
				 	k+=1
			if c<255:
			    l=defaultsubnet[2]
			    def_sub=defaultsubnet[2]
			elif c<65025:
			    l=defaultsubnet[1]
			    def_sub=defaultsubnet[1]
			elif c<16581375:
			    l=defaultsubnet[0]
			    def_sub=defaultsubnet[0]
			e=(32-k)*"1"
			f=k*'0'
			g=e+f
			i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
			j=subnet[l]
			bin_rep=g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::])
			h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
			new_sub='.'.join(h)
			prefix_len=i.count('1')
			z=i.count('1')-j.count('1')
			networks=int(2**(z))
			hosts=c
			data=[def_sub,bin_rep,new_sub,prefix_len,networks,hosts]
			results.append(data)
		#print(results)
		return render_template("about.html",results=results)		
	return render_template("about.html")

@app.route("/manual",methods=["GET","POST"])
def manual_ip():
	if request.method=="POST":
		ips=request.form['ip']
		hosts=int(request.form['host'])
		results=[]
		l=ips.split('/')
		ip_address=l[0].split('.')
		if len(l)==2 and len(ip_address)==4:
			pre_len=int(l[1])
			hh=ip_address
			ls=[]
			k=1
			ww=1
			while True:
				ss=2**ww
				if ss>hosts:
					break
				ww+=1
			while True:
				c=2**k
				if c>=int(l[1]):
					break
				k+=1
			e=(32-k)*"1"
			f=k*'0'
			g=e+f
			h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
			subnetmask='.'.join(h)
			for v in range(len(ip_address)):
				z=int(ip_address[v])
				ls.append(z)
				m=[]
				main=[]
			if int(ip_address[0])>=0 and int(ip_address[0])<=127:
				p=8
				nb=pre_len-p
				hb=32-pre_len
				new_nb=int(hb-ww)
			elif int(ip_address[0])>=128 and int(ip_address[0])<=191:
				p=16
				nb=pre_len-p
				hb=32-pre_len
				new_nb=int(hb-ww)
			elif int(ip_address[0])>=192 and int(ip_address[0])<=223:
				p=24
				nb=pre_len-p
				hb=32-pre_len
				new_nb=hb-ww
			networkcount=int(2**new_nb)
			hostcount=(2**ww)-2
			e=((32-k)+new_nb)*"1"
			f=ww*'0'
			g=e+f
			h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
			newsubnet='.'.join(h)
			for j in range(1,int(2**new_nb)+1):
				for g in range((hosts+3)):
					m.append('.'.join(hh))
					ls[-1]=ls[-1]+1
					hh[-1]=str(ls[-1])
					if ls[-1]==256:
						ls[-2]=ls[-2]+1
						hh[-2]=str(ls[-2])
						ls[-1]=0
						hh[-1]=str(ls[-1])
					if ls[-2]==256:
						ls[-3]=ls[-3]+1
						hh[-3]=str(ls[-3])
						ls[-2]=0
						hh[-2]=str(ls[-2])
					if ls[-3]==256:
						ls[0]=ls[0]+1
						hh[0]=str(ls[0])
						ls[-3]=0
						hh[-3]=str(ls[-3])
				Network=j
				Network_id=m[0]
				broadcast_id=m[-1]
				usable_ip=m[1],"-",m[-2]
				main.append(m)
				m=[]
				data=[subnetmask,networkcount,hostcount,newsubnet,Network,Network_id,broadcast_id,usable_ip]
				results.append(data)
			#print(Network,newsubnet,networkcount)
			return render_template("manual.html",results=results)
	return render_template("manual.html")
@app.route("/manualip",methods=["GET","POST"])
def manualip():
	if request.method=="POST":
		ips=request.form['ip']
		l=ips.split('/')
		ip_address=l[0].split('.')
		results=[]
		hh=ip_address
		ls=[]
		k=1
		while True:
			c=2**k
			if c>=int(l[1]):
				break
			else:
				k+=1
		e=(32-k)*"1"
		f=k*'0'
		g=e+f
		h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
		newsubnet=".".join(h)
		for v in range(len(ip_address)):
			z=int(ip_address[v])
			ls.append(z)
			pre_len=int(l[1])
			m=[]
			main=[]
		if int(ip_address[0])>=0 and int(ip_address[0])<=127:
			p=8
			nb=pre_len-p
			hb=32-pre_len
		elif int(ip_address[0])>=128 and int(ip_address[0])<=191:
			p=16
			nb=pre_len-p
			hb=32-pre_len
		elif int(ip_address[0])>=192 and int(ip_address[0])<=223:
			p=24
			nb=pre_len-p
			hb=32-pre_len
		networkcount=int(2**nb)
		hostcount=(2**hb)-2
		i=0
		hh[-1]='0'
		for j in range(1,int(2**nb)+1):
			for g in range(2**hb):
				m.append('.'.join(hh))
				i+=1
				hh[-1]=str(i)
				if i==256:
					ls[-2]=ls[-2]+1
					hh[-2]=str(ls[-2])
					i=0
				if ls[-2]==256:
					ls[-3]=ls[-3]+1
					hh[-3]=str(ls[-3])
					ls[-2]=0
			Network=j
			Network_ID=m[0]
			Broadcast_ID=m[-1]
			Usableip=m[1],"-",m[-2]
			main.append(m)
			m=[]
			data=[newsubnet,networkcount,hostcount,Network,Network_ID,Broadcast_ID,Usableip]
			results.append(data)
		return render_template("manualip.html",results=results)
	return render_template("manualip.html")
if __name__=="__main__":
	app.run(debug=True)