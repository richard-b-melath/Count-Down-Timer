import time

starttime = input('Enter the start time in "HH/MM/SS" format : ')
h,m,s = starttime.split("/")
i,j,k = int(h), int(m), int(s)
print("{:02d}".format(i),"/","{:02d}".format(j),"/","{:02d}".format(k))
if j > 60 or k > 60:
    print("Enter a valid time")
else:
    while i>=00:
        while j>=00:
            while k>=00:
                print("\rTime remaining : ", "{:02d}".format(i),"/","{:02d}".format(j),"/","{:02d}".format(k), end="", flush=True)
                time.sleep(1)
                k -= 1
            j -= 1
            k = 60
        i -= 1
        j = 60

    print("\n\nTime Stopped\n\n")