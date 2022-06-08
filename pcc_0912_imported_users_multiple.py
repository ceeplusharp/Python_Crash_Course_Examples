# Chapter 9: Try it Yourself. 9-12: Multiple Modules.

from pcc_0912_module_admin import Admin


# Output using Child Class Admin
admin1 = Admin('Princess', 'Carolyn', 'Hollywoo', 26)

admin1.describe_user()
admin1.greet_user()

admin1.show_privileges('can add post')
admin1.show_privileges('can delete post')
admin1.show_privileges('can ban user')

# Output using Child Class Admin and New Class Privileges1
admin2 = Admin('Dianne', 'Nguyen', 'Boston', 32)

admin2.describe_user()
admin2.greet_user()

admin2.privileges1.show_privileges1('can add post')
admin2.privileges1.show_privileges1('can delete post')
admin2.privileges1.show_privileges1('can ban user')
