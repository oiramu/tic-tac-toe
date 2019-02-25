import aiml

print("\n=============== Bienvenido a T, Tu Asistente Personal ===============\n")

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("test.xml")
kernel.learn("test2.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    print(kernel.respond(input("Enter your message >> ")))


