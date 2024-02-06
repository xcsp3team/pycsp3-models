from pycsp3.problems.data.parsing import *

nNodes = number_in(line())
M = number_in(next_line())
nDomains = number_in(next_line())
data['domain_link_weights'] = split_with_rows_of_size(numbers_in(next_line()), nDomains)
assert nDomains == len(data['domain_link_weights'])
nLinks = number_in(next_line())
data['node_links'] = decrement(split_with_rows_of_size(numbers_in(next_line()), 2))
assert nLinks == len(data['node_links'])
data['nodes'] = decrement(split_with_rows_of_size(numbers_in(next_line()), 8))
assert nNodes == len(data['nodes'])
data['start_domain'] = number_in(next_line()) - 1
data['target_domain'] = number_in(next_line()) - 1
vnflist_size = number_in(next_line())
data['vnflist'] = decrement(numbers_in(next_line()))
assert vnflist_size == len(data['vnflist'])
data['vnf_arcs'] = decrement(split_with_rows_of_size(numbers_in(next_line()), 2))
assert vnflist_size - 1 == len(data['vnf_arcs'])
data['proximity_to_source'] = numbers_in(next_line())
data['proximity_to_destination'] = numbers_in(next_line())
assert vnflist_size == len(data['proximity_to_source']) == len(data['proximity_to_destination'])
n_domain_constraints = number_in(next_line())
data['domain_constraints'] = decrement(split_with_rows_of_size(numbers_in(next_line()), 4))
assert n_domain_constraints == len(data['domain_constraints'])
