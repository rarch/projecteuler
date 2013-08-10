HC=ghc

HSOUTPUTDIR=hs_output
HSSUFF=_hs.out

NAME=seven
UTILDIR=../util
UTIL=util

HSSRC=$(NAME).hs
HSSRCS=$(HSSRC) $(UTILDIR)/$(UTIL).hs

all: haskell
rm: rm_haskell
clean: clean_haskell
	
haskell: $(NAME)
$(NAME): $(HSSRCS)
	@rm -f $@
	$(HC) --make $@ -o $(NAME)$(HSSUFF) -i$(UTILDIR) -outputdir $(HSOUTPUTDIR)

clean_haskell:
	rm -rf $(HSOUTPUTDIR)
	
rm_haskell:
	@make clean
	rm -f $(NAME)$(HSSUFF)

.PHONY: all clean haskell rm clean_haskell rm_haskell