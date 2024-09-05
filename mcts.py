import random 
import copy
import math

import graphviz

random.seed(42)


class MCTS:
    def __init__(self, state, max_iterations=1000):
        self.root = Node(state)
        self.max_iterations = max_iterations

    def rollout(self, node):
        temp = copy.deepcopy(node.state)
        while not temp.is_game_over():
            temp.make_move(random.choice(temp.valid_moves()))
        return temp.check_winner()

    def run(self):
        for i in range(self.max_iterations):
            current = self.root

            while current.nodes:
                current = max(current.nodes, key=lambda x: x.UCB1())

            # print("Selected", current)

            if current.visits == 0:
                winner = self.rollout(current)
                current.backpropagate(winner)
            elif not current.state.is_game_over():
                current.expand()
                current = current.nodes[0]
                winner = self.rollout(current)
                current.backpropagate(winner)
            elif current.state.is_game_over():
                winner = current.state.check_winner()
                current.backpropagate(winner)
            else:
                print("skipped", i)


class Node:
    def __init__(self, state, prev=None):
        self.prev = prev
        self.state = state
        self.nodes = []
        self.visits = 0
        self.wins = {"X": 0, "O": 0, None: 0}
        self.focus_player = "X"
        self.ucb1 = None

    def expand(self):
        if self.nodes == []:
            for move in self.state.valid_moves():
                new_state = copy.deepcopy(self.state)
                new_state.make_move(*move) if isinstance(move, (list, tuple)) else new_state.make_move(move)
                self.nodes.append(Node(new_state, self))

    def backpropagate(self, winner):
        self.visits += 1
        self.wins[winner] += 1
        if self.prev:
            self.prev.backpropagate(winner)

    def UCB1(self):
        if self.visits != 0:
            prev_visits = self.prev.visits if self.prev else self.visits
            return round(self.wins[self.focus_player] / self.visits + (2 * (math.log(prev_visits) / self.visits) ** 0.5), 3)
        return float("inf")

    def draw_tree(self, alpha_of="visits", max_alpha=None):
        if max_alpha is None:
            max_alpha = self.__dict__[alpha_of]
        alpha = self.__dict__[alpha_of] / max_alpha
        fillcolor = f"{int(255 * (1 - alpha)):02x}0000{int(255 * alpha):02x}"
        if dot is None:
            dot = graphviz.Digraph()
        dot.node(str(id(self.node)), str(self.node), fillcolor=fillcolor)
        for child in self.node.nodes:
            dot.edge(str(id(self.node)), str(id(child)))
            self.draw_tree(child, dot, max_alpha)
        return dot
    
    def print_tree(self, depth=0):
        print("  " * depth, depth, str(self))
        for child in self.nodes:
            child.print_tree(depth + 1)
    
    def __repr__(self) -> str:
        # return f"Node({self.state}, {self.visits}, {self.wins}), {self.UCB1()}"
        return f"{self.state}, {self.UCB1()}"


def draw_tree(node, dot=None, alpha_of="visits", max_alpha=None):
    if max_alpha is None:
        max_alpha = node.__dict__[alpha_of]
    alpha = (node.__dict__[alpha_of] / max_alpha)

    red, green, blue = 255, 0, 0

    color = f"#{red:02x}{green:02x}{blue:02x}{int(alpha * 255):02x}"

    if dot is None:
        dot = graphviz.Digraph()
        dot.attr(ranksep='1', nodesep='0.15')
    dot.node(str(id(node)), str(node), fillcolor=color, style="filled")
    for child in node.nodes:
        dot.edge(str(id(node)), str(id(child)))
        draw_tree(child, dot, max_alpha=max_alpha)
    return dot
