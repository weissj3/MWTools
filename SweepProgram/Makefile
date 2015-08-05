CC=g++
CXXFLAGS=-I. -Wall -g

DEPS = Util.h Sweep.h RunInstance.h Scheduler.h

OBJ = main.o Sweep.o Util.o RunInstance.o Scheduler.o


%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CXXFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CXXFLAGS)

.PHONY: clean

clean:
	rm -f *.o *~ core list.txt separation_checkpoint results.txt main
