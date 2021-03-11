# for i in range(1,121):
#     print(f"{i}.jpg")

import os
for i in range(1,121):
    os.rename(f"images/img ({i}).jpg", f"images/{i}.jpg")
    