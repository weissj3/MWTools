CC=g++
CFLAGS=-I. -Wall

DEPS = Util.h Sweep.h RunInstance.h Scheduler.h

OBJ = main.o Sweep.o Util.o RunInstance.o Scheduler.o


%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f *.o *~ core list.txt separation_checkpoint results.txt main
