CC=g++
CFLAGS=-I. -Wall -g

DEPS = Util.h Hessian.h RunInstance.h Scheduler.h BasicMWClass.h

OBJ = main.o Hessian.o Util.o RunInstance.o Scheduler.o BasicMWClass.o


%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f *.o *~ core list.txt separation_checkpoint results.txt main
