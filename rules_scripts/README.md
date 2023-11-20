
#如果创建只允许访问Google.com的规则

1.	在可以使用aws cli的机器上，运行代码创建firewall policy以及3个rule groups，此脚本会创建以下rule groups：

-	AllowSSH100           Allow SSH any any
-	AllowGoogleDomain100  允许访问google
-	AllowICMP100		        允许访问ICMP any any

以及一个叫'MyPolicy100'的firewall policy，此policy会绑定的上述三个rule group


2.	进入firewall，找到Firewall Policy，点击右边Edit

![image](https://github.com/AutoJunjie/aws-networkfirewall-cfn-templates/assets/38706868/8e90f7ad-e649-4971-9b51-00c360a69ecf)

选择脚本创建好的Policy100，点击save changes

![image](https://github.com/AutoJunjie/aws-networkfirewall-cfn-templates/assets/38706868/89007a0a-12c4-48fd-8b7e-e22d9994c9d7)

3.	等待sync state到in-sync状态

![image](https://github.com/AutoJunjie/aws-networkfirewall-cfn-templates/assets/38706868/d9f6fbc7-2620-4247-90f6-49668407ca00)

完成，可以进行测试

