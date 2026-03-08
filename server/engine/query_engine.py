from .intent_parser import IntentParser
from .graph_retriever import GraphRetriever
from .vector_retriever import VectorRetriever
from .synthesizer import Synthesizer

class QueryEngine:
    def __init__(self):
        self.intent_parser = IntentParser()
        self.graph_retriever = GraphRetriever()
        self.vector_retriever = VectorRetriever()
        self.synthesizer = Synthesizer()

    def query(self, query, filters):
        intent = self.intent_parser.parse(query)
        graph_context = self.graph_retriever.retrieve(intent, filters)
        vector_chunks = self.vector_retriever.retrieve(query, filters)
        answer = self.synthesizer.synthesize(query, graph_context, vector_chunks)
        return answer
