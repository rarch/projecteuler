HC=ghc
HC_OPTS=-cpp

NAME=two
UTILDIR=../util
UTIL=util

SRC=$(NAME).hs
SRCS=$(SRC) $(UTILDIR)/$(UTIL).hs

OBJ=$(NAME).o
OBJS=$(OBJ) $(UTILDIR)/$(UTIL).o

HI=$(NAME).hi
HIS=$(HI) $(UTILDIR)/$(UTIL).hi

# will eventually have to separate hs obj files from other obj files

all: haskell
	
haskell: $(NAME)
$(NAME): $(SRCS)
	@rm -f $@
	@# $(HC) --make $(SRCS) -o $(NAME)
	$(HC) --make $(SRC) -i$(UTILDIR) -o $(NAME)

clean:
	rm -f $(OBJ) $(HI)
	
rm:
	rm -f $(OBJS) $(HIS)
	rm -f $(NAME)

.PHONY: clean all rm