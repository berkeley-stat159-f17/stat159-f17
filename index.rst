.. Stat 159/259 - Reproducible and Collaborative Data Science documentation master file, created by
   sphinx-quickstart on Tue Sep  5 00:56:03 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Stat 159/259 - Reproducible and Collaborative Data Science
==========================================================

All materials for this course are `available on GitHub <https://github.com/berkeley-stat159-f17/stat159-f17>`_.

The `class syllabus <_static/ref/syllabus.pdf>`_ will be updated over the course of the first couple of weeks of class.

Readings
~~~~~~~~

* Due **Monday** Sept 25, 2017:

  - `Treating Code As an Essay <http://proquest.safaribooksonline.com/9780596510046/treating_code_as_an_essay>`_, by Yukihiro Matsumoto (aka "Matz"). Matz is the creator of Ruby and the essay talks about Ruby, but its ideas have generic value.

  - `Python’s Dictionary Implementation: Being All Things to All People <http://proquest.safaribooksonline.com/9780596510046/pythons_dictionary_implementation_being_all_things_to_all_peopl>`_, by Andrew Kuchling. An essay that discusses the most important data structure in Python, the Dictionary.  In general we will not be diving deeply into technical implementation and programming details, but knowing a little bit about one of the key parts of the language is valuable.

* Due Sept 14, 2017. Three short papers about the scientific Python ecosystem and IPython/Jupyter: 

  - `IPython: A System for Interactive Scientific Computing <http://fperez.org/papers/ipython07_pe-gr_cise.pdf>`_.
  - `Python: An Ecosystem for Scientific Computing <http://fperez.org/papers/perez11_cise_python_ecosystem.pdf>`_.  
  - `Jupyter Notebooks—a publishing format for reproducible computational workflows <http://fperez.org/papers/kluyver16-jupyter-nb-repro.pdf>`_.

* Due Sept 7, 2017: `Developing open source scientific practice <_static/ref/millman-perez.pdf>`_.

* Due Oct 10th, 2017 (for guest lecture by Stuart Geiger):

  - This lecture will be an inside look into a reproducible research project studying conflict between automated software agents (or bots) in Wikipedia. Spend however much time you'd normally spend preparing for this class browsing through Wikipedia's public but behind-the-scenes spaces to get a general background on what bots do and how the community governs them. 
  
  - Core readings
  
    - `Introduction to Wikipedia Bots <https://en.wikipedia.org/wiki/Wikipedia:Bots>`_
    
       - This page contains many links to pages you might find interesting, including a list of bots
       
    - `The Bot Policy <https://en.wikipedia.org/wiki/Wikipedia:Bot_policy>`_.
    - `Recent bot edits to English Wikipedia articles <https://en.wikipedia.org/wiki/Special:RecentChanges?limit=500&days=7&urlversion=2&hidehumans=1&hideWikibase=1&hidelog=1&hidecategorization=1&hidenewpages=1&namespace=0>`_.
    
      - Click "diff" on each line to get a diff of what the bot changed
      - Click "hist" to see the history of edits to that artcile
      - Click the bot's username to get their user talk page
      - This is a version control system!
      
  - Some additional materials if you are interested further:
  
    - `ClueBot NG <https://en.wikipedia.org/wiki/User:ClueBot_NG>`_ (an anti-spam/vandalism bot using machine learning and neural networks)
    - `AnomieBOT's tasklist <https://en.wikipedia.org/wiki/User:AnomieBOT/TaskList>`_ (a bot account used for many different tasks).
    - `Double redirects <https://en.wikipedia.org/wiki/Wikipedia:Double_redirects>`_ (a task frequently automated with bots that features in the paper).
    - `Requests for Arbitration: Betacommand 2 <https://en.wikipedia.org/wiki/Wikipedia:Requests_for_arbitration/Betacommand_2>`_ (the Arbitration Committee is like Wikipedia's Supreme Court, this was a controversial case about a bot developer)

Lectures
~~~~~~~~

.. toctree::
   :maxdepth: 1
   :glob:

   lectures/01-git/Git-Tutorial.ipynb
   lectures/02-ipython/Index.ipynb
   lectures/03-reading1-discussion.ipynb
   lectures/04-reading2-discussion.ipynb
   lectures/05-class-practice.ipynb

Labs
~~~~

.. toctree::
   :glob:
   :maxdepth: 1

   labs/*

Resources
~~~~~~~~~


.. toctree::
   :maxdepth: 1

   resources.md


* :ref:`search`
