# Makefile for lectures presented as slide decks made from notebooks

# List here which lectures should have slides (list the notebooks)

SLIDESNB=14-sphinx.ipynb 15-pvalues/rabbits.ipynb

SLIDES=$(patsubst %.ipynb, %.slides.html, $(SLIDESNB))

slides: $(SLIDES)

.PHONY: clean

clean:
	rm -f $(SLIDES)

# Suffix rules

%.slides.html: %.ipynb
	jupyter nbconvert --to slides --reveal-prefix \
	"https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.1.0" $<

