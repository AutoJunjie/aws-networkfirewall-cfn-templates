
如果创建只允许访问Google.com的规则

1.	在可以使用aws cli的机器上，运行代码创建firewall policy以及3个rule groups，此脚本会创建以下rule groups：

-	AllowSSH100                      #Allow SSH any any
-	AllowGoogleDomain100  #允许访问google
-	AllowICMP100		#允许访问ICMP any any

以及一个叫'MyPolicy100'的firewall policy，此policy会绑定的上述三个rule group


2.	进入firewall，找到Firewall Policy，点击右边Edit

 

选择脚本创建好的Policy100，点击save changes

 


3.	等待sync state到in-sync状态

 


完成，可以进行测试
![image](https://github.com/AutoJunjie/aws-networkfirewall-cfn-templates/assets/38706868/1faca152-4734-4c43-94f5-fa260870add9)
