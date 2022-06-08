# Chapter 9: Try it Yourself. 9-11: Imported Admin.

import pcc_0911_users_module as users

# Output using Child Class Admin
admin1 = users.Admin('Princess', 'Carolyn', 'Hollywoo', 26)

admin1.describe_user()
admin1.greet_user()

admin1.show_privileges('can add post')
admin1.show_privileges('can delete post')
admin1.show_privileges('can ban user')

# Output using Child Class Admin and New Class Privileges1
admin2 = users.Admin('Dianne', 'Nguyen', 'Boston', 32)

admin2.describe_user()
admin2.greet_user()

admin2.privileges1.show_privileges1('can add post')
admin2.privileges1.show_privileges1('can delete post')
admin2.privileges1.show_privileges1('can ban user')
