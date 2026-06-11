raw= "  ERROR:2026-06-11:Connection_Timeout_On_Server_01  "
raw=raw.strip() #.strip() removes leaidng and tailing whitespace
print(raw)

cleaned=raw.lower()

a,b,c=cleaned.split(":")
final=c.replace("_"," ")

print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(f"final:{final}")

w,x,y,z, *extra=final.split(" ")
print(f"w:{w}, x:{x}, y:{y}, z:{z}")