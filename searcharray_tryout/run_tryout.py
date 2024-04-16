from searcharray import SearchArray
from searcharray.similarity import bm25_legacy_similarity

from searcharray_tryout.util import ws_punc_tokenizer

if __name__ == '__main__':
    docs = ['Life is good', 'Search is my life']
    input_indexed = SearchArray.index(docs, tokenizer=ws_punc_tokenizer)

    print(input_indexed.shape)
    print(input_indexed.term_dict)
    print(input_indexed.term_mat)
    print(input_indexed.posns.encoded_term_posns)

    print(type(input_indexed))

    term_id = input_indexed.term_dict.get_term_id('life')
    doc_ids, term_frequencies = input_indexed.posns.termfreqs(term_id)
    print(f"doc_ids: {doc_ids}")
    print(f"term frequencies: {term_frequencies}")

    query = 'my life'
    tok_query = ws_punc_tokenizer(query)
    matches = input_indexed.match(tok_query)
    print(matches)

    # Calculate the score for the provided query
    query = 'my life'
    tok_query = ws_punc_tokenizer(query)
    bm25_score = input_indexed.score(tok_query)
    print(bm25_score)

    custom_bm25_score = bm25_legacy_similarity(k1=5, b=0.75)
    bm25_custom_score = input_indexed.score(tok_query, custom_bm25_score)
    print(bm25_custom_score)