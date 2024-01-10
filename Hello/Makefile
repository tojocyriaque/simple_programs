nm = hello
src = src/$(nm).asm
bin = bin/$(nm)

exec:
	nasm -f elf $(src)
	mv src/$(nm).o src/obj

	ld -m elf_i386 -s -o $(bin) src/obj/$(nm).o

clean:
	-rm src/obj/*
	-rm bin/*
