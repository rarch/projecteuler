HC=ghc
HC_OPTS=-cpp

NAME=one
SRCS=$(NAME).hs
OBJS=$(NAME).o
HIS=$(NAME).hi

# will eventually have to separate hs obj files from other obj files

all: haskell
	
haskell: $(NAME)
$(NAME): $(SRCS)
	@rm -f $@
	$(HC) --make $@ -o $(NAME)

clean:
	rm -f $(OBJS) $(HIS)
	
rm:
	@make clean
	rm -f $(NAME)

.PHONY: all clean haskell rm