# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 09:32:45 2016

@author: Aaron
"""

## PROGRAM TO TRANSLATE YOU TO I UPDATED (9/11/2016)
#def translated():
##INPUT LEVEL OF TRANSLATION 0 - 8, RETURN TRANSLATED, PRONOUN RATIOS 
    
#level1 = input('YOU(1), THEY(2), HE/SHE(3), WE(4), ONE(5), IT(6), THE(7) : ')    
#level = int(level1)
level = 7   
import string

import nltk
from nltk import Text
from nltk import word_tokenize
from nltk import FreqDist
import tkinter as tk
from spacy.en import English
nlp = English()
parser = English()

#    from nltk.collocations import *
#    bigram_measures = nltk.collocations.BigramAssocMeasures()
#    trigram_measures = nltk.collocations.TrigramAssocMeasures()


#LETS FUNCTION CALLING
#from drf import choose_file, comment_strip, namo
#from drf import *
#a = choose_file()
#NAME = namo(a)
#comments = comment_strip(a, NAME)

#comments = """
#    You are so amazingly beautiful. I want you. 
#    I want to look deep into your eyes and feel your body close to mine.
#    I love you so much, I want to kiss you. I want to touch all over your 
#    entire body.”"""

#comments = """I am not a troll, you are. 
#    You lie and cheat and steal from everyone. 
#    They are fat and lazy. 
#    All they do is smoke pot all day and worship satan.
#    Let those soulless fuckheads rot in Hell for eternity!"""
#add final word to prevent out of index error
comments = ''
comments = comments + ' ! '
def Translated(comments):
#DO THE TRANSLATION...
    text4 = comments.lower()
    text = text4
    tokens = nltk.wordpunct_tokenize(text) 
    tokens_new = tokens
    #TRANSLATION FILTER YOU, THEY, WE
    #LEVEL !, YOU TRANSLATIONS
    #print('level = ', level)
    for index, w in enumerate(tokens_new):
        for levels in range(level):
            if level == 0:
                break    
            if w == 'you':
                tokens_new[index] = 'I'
            if w == 'u':
                tokens_new[index] = 'I'
            if w == 'your':
                tokens_new[index] = 'MY'
            if w == 'yours':
                tokens_new[index] = 'MINE'
            if w == 'yourself':
                tokens_new[index] = 'MYSELF'
            if w == 'yourselves':
                tokens_new[index] = 'MYSELF'
            ##WORD REMOVE FOR TEMP FILES    
            if w == 'thephoenixrises':
                tokens_new[index] = ''
            if level == 1:
                break       
            if w == 'they':
                tokens_new[index] = 'I'
            if w == 'them':
                tokens_new[index] = 'ME'
            if w == 'their':
                tokens_new[index] = 'MY'
            if w == 'theirs':
                tokens_new[index] = 'MINE'
            if w == 'themselves':
                tokens_new[index] = 'MYSELF'
            if w == 'theirselves':
                tokens_new[index] = 'MYSELF'
            if w == 'theirself':
                tokens_new[index] = 'MYSELF'
            if w == 'themself':
                tokens_new[index] = 'MYSELF'
            if level == 2:
                break        
            if w == 'he':
                tokens_new[index] = 'I'
            if w == 'him':
                tokens_new[index] = 'ME'    
            if w == 'his':
                tokens_new[index] = 'MY'
            if w == 'himself':
                tokens_new[index] = 'MYSELF'
            if w == 'she':
                tokens_new[index] = 'I'
            if w == 'her':
                tokens_new[index] = 'MY'    
            if w == 'hers':
                tokens_new[index] = 'MINE'
            if w == 'herself':
                tokens_new[index] = 'MYSELF'    
            if level == 3:
                break       
            if w == 'we':
                tokens_new[index] = 'I'
            if w == 'us':
                tokens_new[index] = 'ME'    
            if w == 'our':
                tokens_new[index] = 'MY'
            if w == 'ours':  
                tokens_new[index] = 'MINE'
            if w == 'ourself':
                tokens_new[index] = 'MYSELF'
            if w == 'ourselves':
                tokens_new[index] = 'MYSELF'
            if level == 4:
                break 
            if w == 'one':
                tokens_new[index] = 'I'
            if w == 'people':
                tokens_new[index] = 'I'
            if w == 'everyone':
                tokens_new[index] = 'I'
            if w == 'someone':
                tokens_new[index] = 'I'
            if level == 5:
                break    
            if w == 'it':
                tokens_new[index] = 'I'
            if w == 'its':
                tokens_new[index] = 'MY'    
            if w == 'itself':
                tokens_new[index] = 'MYSELF'
            if level == 6:
                break    
#            if w == 'a':
#                tokens_new[index] = 'MY'
            if w == 'the':
                tokens_new[index] = 'MY'    
#            if w == 'an':
#                tokens_new[index] = 'MY'
            if w == 'those':
                tokens_new[index] = 'MY'
            if level == 7:
                break
    
    doc = nlp.tokenizer.tokens_from_list(tokens_new)    
    parsed_text = parser(doc.text)
    newtext = [0]*len(parsed_text)
    #REPLACE NOUNS WITH SELF
    
    #FIRST GET NOUNS
    jj = 0
    whatiam = {}
    for ip in range(len(parsed_text)):
        #print(txt)
        #subject would be
        if parsed_text[ip].pos_ == "NOUN" and len(parsed_text[ip].orth_) > 2:
            #newtext[it] = 'SELF'
            #print('I AM ', parsed_text[ip], ' NOUN')
            whatiam[jj] = parsed_text[ip]
            jj += 1
                #print(newtext[it])
        if parsed_text[ip].pos_ == "ADJ" and len(parsed_text[ip].orth_) > 2:
            #newtext[it] = 'SELF'
            #print('I AM ', parsed_text[ip], ' ADJ')
            whatiam[jj] = parsed_text[ip]
            jj += 1
                #print(newtext[it])
    print('')
    if level >= 8:
        for it in range(len(parsed_text)):
        #print(txt)
        #subject would be
            if parsed_text[it].pos_ == "NOUN" and len(parsed_text[it].orth_) > 2:
                newtext[it] = 'SELF'
                #print('I AM ', parsed_text[it])
                #print(newtext[it])
    
            else:
                newtext[it] = str(parsed_text[it]) 
                #print(parsed_text[it])    
    
    #FIND SUBJECT AND KEEP AS I, then change all other instances of I to MYSELF 

    #get token dependencies
    for ie in range(len(parsed_text)):
        #print(txt)
        #subject would be
        if parsed_text[ie].dep_ == "nsubj" and str(parsed_text[ie]) == 'I':
            subject = parsed_text[ie].orth_
            newtext[ie] = str(parsed_text[ie])
            #print(parsed_text[ie])
            #print(subject, '  SUBJECT')
        #iobj for indirect object
        if parsed_text[ie].dep_ != "nsubj" and str(parsed_text[ie]) == 'I' :
            #print(parsed_text[ie])
            #print('MYSELF')
            newtext[ie] = 'MYSELF'    
        elif level < 8:
            newtext[ie] = str(parsed_text[ie]) 
            #print(parsed_text[ie])
    #print(newtext)
    #print(tokens_new)
    #newtext = str(newtext)
    #REPLACE ARE, IS AFTER I WITH AM            
    from nltk import FreqDist
    from nltk import Text  
    #textX = Text(nltk.wordpunct_tokenize(text))
    tokens_new = newtext
    textTo = Text(tokens_new)
    #textTo = Text(newtext)
    c = nltk.ConcordanceIndex(textTo.tokens, key = lambda s: s.lower())
    ind_I =  c.offsets('I')
    #print(ind_I)
           

    after_words = ([textTo.tokens[offset+1] for offset in c.offsets('I')])
    ind_aw = [x+1 for x in ind_I]
    for index, w in enumerate(after_words):
            if w == 'are':
                after_words[index] = 'AM'
            elif w == 'is':
                after_words[index] = 'AM'
            elif w == 'r':
                after_words[index] = 'AM'
            elif w == 'all':
                after_words[index] = ''
            elif w == 'else':
                after_words[index] = ''
    for i, w in enumerate(after_words):
         tokens_new[ind_aw[i]] = after_words[i]
         #newtext[ind_aw[i]] = after_words[i]
         
    before_words = ([textTo.tokens[offset-1] for offset in c.offsets('I')])         
    ind_bw = [x-1 for x in ind_I]
    for index, w in enumerate(before_words):
            if w == 'are':
                before_words[index] = 'AM'
            elif w == 'is':
                before_words[index] = 'AM'
            elif w == 'r':
                before_words[index] = 'AM'
    for i, w in enumerate(before_words):
         tokens_new[ind_bw[i]] = before_words[i]
         #newtext[ind_bw[i]] = before_words[i]
    
    ind_aw2 = [x+2 for x in ind_I]     
    after_words2 = ([textTo.tokens[offset+2] for offset in c.offsets('I')])
    #after_words2 = (textTo.tokens[ind_aw2] for ind in ind_aw2)
    for index, w in enumerate(after_words2):
            if w == 're':
                after_words2[index] = 'M'
            elif w == 's':
                after_words2[index] = 'M'
    for i, w in enumerate(after_words2):
         tokens_new[ind_aw2[i]] = after_words2[i]
            
                
    #GET ACTUAL WORDCOUNT
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text1 = str(tokens_new).translate(translator)
    text2 = word_tokenize(text1)
    word_count = len(text2)
    #print('Word Count :', word_count)  
    #print(' ')
    
    #PRINT TRANSLATION
    translated = ' '.join(tokens_new)
    
#    if level == 0:
#        print('***level 0 NO translation***')
#    if level == 1:
#        print('***level 1 YOU translation***')
#    if level == 2:
#        print('***level 2 YOU, THEY translation***')
#    if level == 3:
#        print('***level 3 YOU, THEY, HE/SHE translation***')
#    if level == 4:
#        print('***level 4 YOU, THEY, HE/SHE, WE translation***')
#    if level == 5:
#        print('***level 5 YOU, THEY, HE/SHE, WE, ONE translation***')
#    if level == 6:
#        print('***level 6 YOU, THEY, HE/SHE, WE, ONE, IT translation***')
#    if level > 6:
#        print('***level 7 YOU, THEY, HE/SHE, WE, ONE, IT, THE translation***')          
          
    #TO RUN CONCORDANCE AND WHATNOT 
    textX = Text(nltk.wordpunct_tokenize(text))
    fdistX = FreqDist(textX)
    
    #CALCULATE _ TO TOTAL RATIO AND PRINT RESULT
    fpS = ['i', 'me', 'my', 'mine', 'myself', 'im']
    sp = ['you', 'your', 'yours', 'yourself', 'yourselves', 
                           'u']
    fpP= ['we', 'us', 'our', 'ours', 'ourselves', 'ourself']
    tpM = ['he', 'his', 'him', 'himself' ]           
    tpF = ['her', 'hers', 'herself']  
    tpNS = ['it', 'its', 'itself' ]      
    tpNP = ['they', 'them', 'their', 'themselves',
                                 'theirselves', 'theirs', 'theirself', 'themself']
    op = ['one', 'someone', 'everyone', 'people']                             
    art = ['the', 'a', 'an']
    
    pnames= ['fpS(I)', 'sp(YOU)', 'fpP(WE)', 'tpM(HE)', 'tpF(SHE)', 
              'tpNP(THEY)', 'op(PPLs)', 'tpNS(IT)', 'art(THE)']        
    psets = [fpS, sp, fpP, tpM, tpF, tpNP, op, tpNS, art]
    pcounts = [0]*len(psets)
    for i in range(len(psets)):
        pcounts[i] = list(range(len(psets[i])))
        for w in range(len(psets[i])):
    #    print(textX.count(first_per_sing_pronouns[w]))
            (pcounts[i])[w] = textX.count((psets[i])[w])
        pcounts[i] = sum(pcounts[i])
    
    tot_counts = sum(pcounts)- pcounts[0]
    #print(NAME)
    #print('TOTAL TOKENS: ', word_count)
    #print('TOTAL TRANSLATED: ', tot_counts, 
    #      'words...',"%.1f" % ((100*tot_counts) / word_count), '%')
          
    
    #NOW CALCULATE RATIOS...COMPARE TO TOTAL
    p_to_tot = [0]*len(pcounts)
   # for i in range(len(pcounts)):    
   #     p_to_tot[i] = (100*pcounts[i] / word_count)
   #     print(pnames[i], 'to TOTAL TOKENS %: ', "%.2f" % p_to_tot[i])
    
    return(translated, whatiam)

[trans, what] = Translated(comments)
#textT = Text(word_tokenize(trans))    
##textT = Text(nltk.wordpunct_tokenize(trans.lower()))
#c = nltk.ConcordanceIndex(textT.tokens, key = lambda s: s.lower())
#after_words = ([textT.tokens[offset+1] for offset in c.offsets('I')])
#a = FreqDist(Text(after_words))
#b = sorted(((a[w],w) for w in a), reverse = TRUE)
#b1 = [(w, i) for i,w in b]
#print('I ANALYSIS')
#print(b1[0:10])

#####    
from textblob import TextBlob
#blob = TextBlob(comments)
blobT = TextBlob(trans)
#d = blob.sentences
dT = blobT.sentences
sent_num = 100
if len(dT) > sent_num:
    for ind in range(sent_num):
        #print(d[ind])
        #print(Translated(str(d[ind])))
        print(dT[ind])
        print('')
#elif sent in blobT.sentences:
#    #print(d)
else:
    for ind in range(len(dT)):
        print(dT[ind])
        print('')    
#
for jk in what.values():
    print('I AM', jk)
print('Number of Sentences: ', len(dT))
print('')

#print(translated[0:3600])

      


