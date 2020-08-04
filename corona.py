from lib import cc, translate
# entire diff: https://www.ncbi.nlm.nih.gov/projects/msaviewer/?rid=7FYNU14F01R&coloring=
# protein alignments: http://virological.org/t/alignment-of-58-sarbecovirus-genomes-for-conservation-analysis-of-sars-cov-2/430
# https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2
# https://www.ncbi.nlm.nih.gov/nuccore/MN908947
# https://zhanglab.ccmb.med.umich.edu/C-I-TASSER/2019-nCov/

# copy machine -- https://www.uniprot.org/uniprot/Q0ZJN1
# zhanglab breaks this down into many more proteins

corona = {}

# begin: 266 base pairs "untranslated"
# https://en.wikipedia.org/wiki/Five_prime_untranslated_region

# https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/

# in front "the untranslated leader sequence that ends with the Transcription Regulation Sequence"
corona['untranslated_region'] = cc[0:265]

corona['orf1a'] = translate(cc[266-1:13483], True)

corona['orf1b'] = translate(cc[13468-1:21555], False).strip("*")  # chop off the stop, note this doesn't have a start

#   S1  = 14-685
#   S2  = 686-1273
#   S2' = 816-1273
corona['spike_glycoprotein'] = translate(cc[21563-1:25384], True)

# Forms homotetrameric potassium sensitive ion channels (viroporin) and may modulate virus release.
corona['orf3a'] = translate(cc[25393-1:26220], True)

# these two things stick out, used in assembly aka they package the virus
corona['envelope_protein'] = translate(cc[26245-1:26472], True)
corona['membrane_glycoprotein'] = translate(cc[26523-1:27191], True)

corona['orf6'] = translate(cc[27202-1:27387], True)

corona['orf7a'] = translate(cc[27394-1:27759], True)
corona['orf7b'] = translate(cc[27756-1:27887], True)  # is this one real?

corona['orf8'] = translate(cc[27894-1:28259], True)

corona['nucleocapsid_phosphoprotein'] = translate(cc[28274-1:29533], True)

# might be called the internal protein (Coronavirus Pathogenesis)
corona['orf10'] = translate(cc[29558-1:29674], True)
