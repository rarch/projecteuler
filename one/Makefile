HC=ghc
HC_OPTS=-cpp

NAME=one
SRCS=$(NAME).hs
OBJS=$(NAME).o
HIS=$(NAME).hi

all: $(NAME)
$(NAME): $(SRCS)
	@rm -f $@
	$(HC) --make $@ -o $(NAME)

clean:
	rm -f $(OBJS) $(HIS)
	
rm:
	@make clean
	rm -f $(NAME)

.PHONY: clean all rm