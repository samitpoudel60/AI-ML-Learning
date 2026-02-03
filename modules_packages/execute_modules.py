from custom_package import math1
##example you want to call another sub package inside the custom package
from custom_package.sub_custom_pack import math2
print(math1.add(11,8))
print(math1.sub(9,4))
##calling the sub package
print(math2.multiply(2,4))