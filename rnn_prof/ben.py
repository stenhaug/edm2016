
import sys
import os
os.chdir("/Users/benastenhaug/Desktop/edm2016/rnn_prof/data")

sys.path.append("/Users/benastenhaug/Desktop/edm2016_lbl/rnn_prof/data")


# need to build up inputs
source = "assistments"
data_file = "skill_builder_data_corrected_big.txt"


class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

common = Bunch(num_folds = 5, item_id_col = "problem_id", remove_skill_nans = False, seed = 0, drop_duplicates = True, max_inter = None, min_inter = 2, proportion_students_retained = 1, output = "irt_result", which_fold = None)

concept_id_col = "single"
template_precision = None
item_precision = None
template_id_col = None
twopo = False

from collections import namedtuple

DataOpts = namedtuple('DataOpts', ['num_folds', 'item_id_col', 'template_id_col', 'concept_id_col',
                                   'remove_skill_nans', 'seed',
                                   'use_correct', 'use_hints', 'drop_duplicates',
                                   'max_interactions_per_user', 'min_interactions_per_user',
                                   'proportion_students_retained'])

data_opts = DataOpts(num_folds=common.num_folds, item_id_col=common.item_id_col,
                         concept_id_col=concept_id_col, template_id_col=template_id_col,
                         remove_skill_nans=common.remove_skill_nans,
                         seed=common.seed, use_correct=True,
                         use_hints=False, drop_duplicates=common.drop_duplicates,
                         max_interactions_per_user=common.max_inter,
                         min_interactions_per_user=common.min_inter,
                         proportion_students_retained=common.proportion_students_retained)

# data, _, ... =

item_id_col = data_opts.item_id_col
template_id_col = data_opts.template_id_col
concept_id_col = data_opts.concept_id_col

interaction_file = data_file
file_path = data_file

import assistments

data, _, _, _, _ = assistments.load_data(
            interaction_file,
            item_id_col=item_id_col,
            template_id_col=template_id_col,
            concept_id_col=concept_id_col,
            remove_nan_skill_ids=data_opts.remove_skill_nans,
            drop_duplicates=data_opts.drop_duplicates,
            max_interactions_per_user=data_opts.max_interactions_per_user,
            min_interactions_per_user=data_opts.min_interactions_per_user)

# data_folds = split_data(data, num_folds=common.num_folds, seed=common.seed)
import splitting_utils
data_folds = splitting_utils.split_data(data, num_folds=common.num_folds, seed=common.seed)


# big run
run_irt.irt(data_folds, common.num_folds, output=common.output, data_opts=data_opts,
                is_two_po=twopo,
                template_precision=template_precision,
                single_concept=concept_id_col is None,
                which_fold=common.which_fold,
                item_precision=item_precision)