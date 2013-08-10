HC=ghc

HSOUTPUTDIR=hs_output
HSSUFF=_hs.out

NAME=five
HSSRC=$(NAME).hs

all: haskell
rm: rm_haskell
clean: clean_haskell
	
haskell: $(NAME)
$(NAME): $(HSSRC)
	@rm -f $@
	$(HC) --make $@ -o $(NAME)$(HSSUFF) -outputdir $(HSOUTPUTDIR)

clean_haskell:
	rm -rf $(HSOUTPUTDIR)
	
rm_haskell:
	@make clean
	rm -f $(NAME)$(HSSUFF)

.PHONY: all clean haskell rm clean_haskell rm_haskell