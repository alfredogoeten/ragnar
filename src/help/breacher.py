#!/usr/bin/env python
#Admin Panel Finder by D3V

import httplib
import socket
import sys


try:                        
    var1=0
    var2=0

    quick = ['admin/','administrator/','admin/login.html','admin/index.html','wp-login.php','admin/admin-login.php','admin-login.php','user.php','adm.php','login.html','administrator.html','login.html','admin.html',
'cp.html','adminpanel.php','admin_login.php']

    regular = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','_admin/','usuarios/',
'usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html', 'adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']  

    ultimate = [ 'admin/slider.php','admin/add-slider.php','admin/add_gallery_image.php','admin/welcome.php','admin/configration.php','admin/dashbord.php','manage_admin.php','admin/form.php','admin/my_account.php','admin/specializations.php',
'admin/initialadmin.php','admin/pages/home_admin.php','admin/home.php','/admin/save.php','admin/enter.php','admin/userpage.php','admin/banners_report.php','admin/login-home.php','admin/category.php','admin/dashboard/index.php','admin/add_banner.php',
'admin/add_testimonials.php','admin/userpage.php','admin_main.html','admin/addblog.php','admin/products.php','admin/admin_management.php','admin/add.php','admin/add-room.php','admin/main_page.php','admin/adminview.php','admin/welcomepage.php','admin/index-digital.php',
'admin/overview.php','admin_home.php','admin/admin_users.php','/admin/upload.php','admin/index_ref.php','admin/checklogin.php','admin/member_home.php','admin/banner.php','admin/manageImages.php','admin/login_success.php','admin/leads.php',
'admin/uhome.html','admin/AdminDashboard.php','admin/cpanel.php','admin/manage_team.php','admin/voucher.php','admin/ManageAdmin.php','admin/dashboard.php','admin/account.php','admin/change_gallery.php','admin/list_gallery.php','admin/viewblog.php','admin/main.php',
'admin/AdminHome.php','admin/dash.php','admin/gallery.php','admin/product.php','admin/loginsuccess.php','admin/gallery.php','admin/headline.php','admin/page_management.php','admin/index.php','admin/event.php','admin/admin-home.php','admin/myaccount.php','admin/admin_index.php',
'admin/viewmembers.php','admin/default.php','admin/CPhome.php','admin/control_pages/admin_home.php','admin/adminarea.php' ]

    try:
        site = raw_input("Enter the target website: ")
        site = site.replace("http://","")
        print ("\t[~]Checking if website is online " + site )
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\t[!] Website is online."
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("\t[!] Error occured, Website offline or invalid URL")
        exit()
    print "1. Quick Scan [Checks for the most common URLs]"
    print "2. Regular Scan [Recommended]"
    print "3. Ultimate Scan [Use if above scans fail]"
    code=input("Enter Scan type: ")
        
    if code==1:
        print("\t[+] Scanning " + site + "...\n")
        for admin in quick:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t[~] Checking " + host )
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\t[!]" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            '''elif response.status == 302:
                                                    print "%s %s" % ("\t[!] " + host, "Possible admin page (302 - Redirect)")
                                                else:
                                                    print "%s %s %s" % ("\t[!] " + host, " Interesting response:", response.status)'''
            connection.close()
        print("\n\tScan Completed \n")
        print var1, " Admin pages found"
        print var2, " Total pages checked"
        raw_input("Press Enter to use Regular Scan")


    if code==2:
        print("\t[+] Scanning " + site + "...\n")
        for admin in regular:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t[~] Checking " + host )
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\t[!]" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\t[!] " + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % ("\t[!] " + host, " Interesting response:", response.status)
            connection.close()
        print("\n\tScan Completed \n")
        print var1, " Admin pages found"
        print var2, " Total pages checked"
        raw_input("Press Enter to use Ultimate Scan")

    if code==3:
        print("\t[+] Scanning " + site + "...\n")
        for admin in ultimate:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t[~] Checking " + host )
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\t[!]" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\t[!] " + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % ("\t[!] " + host, "Interesting response:", response.status)
            connection.close()
        print("\nScan Completed \n")
        print var1, " Admin pages found"
        print var2, " Total pages checked"
        raw_input("Sorry fam! I did my best but failed.")

except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Network error occured! Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Scan Aborted By User"