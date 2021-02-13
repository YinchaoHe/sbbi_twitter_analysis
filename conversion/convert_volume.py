import json
import pickle
import statistics
import pandas as pd
from fuzzywuzzy import process, fuzz


def fraction2decimal(frac_str):
    qtys = frac_str.split('/')
    if len(qtys) == 2:
        numerators = qtys[0].split(" ")
        denominator = int(qtys[1])
        if len(numerators) > 1:
            integ = int(numerators[0])
            numerator = int(numerators[1])
            qty = (1.0 * numerator / denominator) + integ
        else:
            numerator = int(qtys[0])
            qty = 1.0 * numerator / denominator
    elif len(qtys) == 1:
        try:
            numerator = int(qtys[0])
            denominator = 1
            qty = 1.0 * numerator / denominator
        except:
            qty = 0
    return qty

def split_ingr():
    with open('conversion/recipe_ingredients_df.pkl', 'rb') as f:
        recipes = pickle.load(f, encoding="latin1")
    f.close()
    length = recipes.shape[0]
    index = 0
    my_list = list(set(recipes['unit']))
    print(len(my_list))
    new_recipes = []
    amount = length

    with open('conversion/weird_units_list.txt', 'r') as f:
        units= f.readline()
    f.close()
    unit_list = units.split(', ')
    weired_units_arra = unit_list
    weired_units_dic = {}
    weirds = []
    for unit in weired_units_arra:
        weired_units_dic[unit] = []

    while index < length:
        recipe_id = str(recipes.at[index, 'recipe_id'])
        ing_name = recipes.at[index, 'ing_name']
        raw_qty = recipes.at[index, 'qty']
        qty = fraction2decimal(raw_qty)
        unit = recipes.at[index, 'unit']
        if 'pound' in unit:
            qty = qty * 453
            unit = 'gram'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'ounce' in unit:
            qty = qty * 28
            unit = 'gram'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'cup' in unit:
            qty = qty
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'quart' in unit:
            qty = qty * 4
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'gallon' in unit:
            qty = qty * 16
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'tablespoon' in unit:
            qty = qty * 0.0625
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'pint' in unit:
            qty = qty * 2
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'gram' in unit:
            qty = qty
            unit = 'gram'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'liter' in unit:
            qty = qty * 4
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        elif 'teaspoon' in unit:
            qty = qty * 0.02
            unit = 'cup'
            recipes.at[index, 'qty'] = str(qty)
            recipes.at[index, 'unit'] = unit
            recipe = [recipe_id, ing_name, str(qty), unit]
            new_recipes.append(recipe)
        else:
            recipe = [recipe_id, ing_name, str(qty), unit]
            weirds.append(recipe)
            amount -= 1
        index += 1
    print(amount)

    with open('ingr_meta_with_weird_units.json', 'w') as f:
        json.dump(weired_units_dic, f)
    f.close()

    with open('conversion/ingr_major_units.json', 'w') as f:
        data = {}
        data['data'] = new_recipes
        json.dump(data, f)
    f.close()

def add_tag(file1,file2):
    with open(file1, 'r') as f:
        weird_units_dic = json.load(f)
    f.close()

    with open(file2, 'r') as f:
        major_units_dic = json.load(f)
    f.close()

    weird_units = weird_units_dic['data']
    for weird_unit in weird_units:
        weird_unit.append('tag')

    major_units = major_units_dic['data']
    for major_unit in major_units:
        major_unit.append('tag')

    with open(file1, 'w') as f:
        json.dump(weird_units_dic, f)
    f.close()

    with open(file2, 'w') as f:
        json.dump(major_units_dic, f)
    f.close()

def first_step():
    split_ingr()
    add_tag()

def second_step():
    f_recipes = []
    with open('first_step/ingr_major_units.json', 'r') as f:
        raw_recipes = json.load(f)
    f.close()

    with open('first_step/ingr_conv_chart.json', 'r') as f:
        convert_table = json.load(f)
    f.close()

    amount = 0
    for recipe in raw_recipes['data']:
        print(recipe)
        ingr_name = recipe[1]
        qty = float(recipe[2])
        if recipe[-2] == 'cup':
            print(ingr_name)
            m_score = 0
            m_ingr = {}
            for item_dic in convert_table:
                score = fuzz.token_set_ratio(ingr_name, item_dic['name'])
                if m_score < score:
                    m_score = score
                    m_ingr = item_dic
            if m_score > 60:
                print(m_ingr)
                if 'cup' in m_ingr['Volume']:
                    m_volu_info = m_ingr['Volume'].split(" ")
                    m_volu = m_volu_info[0]
                    m_qty = float(m_ingr['Gras'])
                    t_m_volu = fraction2decimal(m_volu)
                    t_m_qty = m_qty / t_m_volu
                    f_m_qty = t_m_qty * qty
                    recipe[2] = str(f_m_qty)
                    recipe[3] = 'gram'
                amount += 1
                print('-' * 50)
                f_recipes.append(recipe)
            else:
                f_recipes.append(recipe)
        else:
            f_recipes.append(recipe)

    with open('second_step/ingr_major_unit2weight.json', 'w') as f:
        data = {}
        data['data'] = f_recipes
        json.dump(data, f)
    f.close()
    print(amount)

def mode_median_replace_solution(path, corect_file, weird_file):
    with open('conversion/' + corect_file, 'r') as f:
        data = json.load(f)
    f.close()
    with open('conversion/' + weird_file, 'r') as f:
        weird_metas = json.load(f)
    f.close()
    print(len(data['data']))
    df = pd.DataFrame(data['data'], columns=['recipe_id', 'ing_name', 'qty', 'unit', 'tag'])

    error_ingr = []
    for weird_unit in weird_metas.keys():
        for weird_meta in weird_metas[weird_unit]:
            if 'rename' in weird_file:
                ref = df.loc[(df['ing_name'] == weird_meta[-1]) & (df['unit'] == 'gram')]

            else:
                ref = df.loc[(df['ing_name'] == weird_meta[1]) & (df['unit'] == 'gram')]
            str_qtys = list(ref['qty'])
            float_qtys = [float(i) for i in str_qtys]
            try:
                qty_mode = statistics.mode(float_qtys)
            except:
                try:
                    qty_mode = statistics.mean(float_qtys)
                except:
                    error_meta = [weird_meta[0], weird_meta[1], weird_meta[2], weird_meta[3], weird_meta[4]]
                    error_ingr.append(error_meta)
                    continue
            corre_meta = [weird_meta[0], weird_meta[1], str(qty_mode), 'gram', weird_meta[4]]
            print(corre_meta)
            data['data'].append(corre_meta)
    print(len(data['data']))
    print(len(error_ingr))

    with open('conversion/' + path + '/new_missmapped_meta.json', 'w') as f:
        errors = {}
        errors['data'] = error_ingr
        json.dump(errors, f)
    f.close()
    with open('conversion/' + path + '/new_corrected_meta.json', 'w') as f:
        json.dump(data, f)
    f.close()
def third_step():
    mode_median_replace_solution(path='third_step', corect_file='second_step/ingr_major_unit2weight.json', weird_file='first_step/ingr_meta_with_weird_units.json')

def rename_missmapping_by_corrected(path, weird_file, correct_file):
    with open('conversion/' + weird_file, 'r') as f:
        missmapping = json.load(f)
    f.close()

    with open('conversion/' + correct_file, 'r') as f:
        ref_metas = json.load(f)
    f.close()

    for meta in missmapping['data']:
        m_score = 0
        m_ingr = {}
        for ref_meta in ref_metas['data']:
            score = fuzz.token_set_ratio(meta[1], ref_meta[1])
            if m_score < score:
                m_score = score
                m_ingr = ref_meta
        if m_score > 60:
            meta[-1] = m_ingr[1]
            print(meta[-1])

    with open('conversion/' + path + '/' + 'rename_missmapped_weird_meta.json', 'w') as f:
        json.dump(missmapping, f)
    f.close()



def forth_step():
    rename_missmapping_by_corrected(path='forth_step', weird_file='third_step/missmapped_meta.json', correct_file='third_step/new_corrected_meta.json')
    mode_median_replace_solution(path='forth_step', weird_file='forth_step/rename_missmapped_weird_meta.json', corect_file='third_step/new_corrected_meta.json')

def split2cupornocup(file, function, path):
    with open('conversion/'+file, 'r') as f:
        data = json.load(f)
    f.close()

    ingrs = []
    if function == 'cup':
        for ingr in data['data']:
            if ingr[3] == 'cup':
                ingrs.append(ingr)

        print(len(ingrs))
        with open('conversion/' + path + '/cup_ingr.json', 'w') as f:
            dic = {}
            dic['data'] = ingrs
            json.dump(dic, f)
        f.close()

    else:
        for ingr in data['data']:
            if ingr[3] != 'cup':
                ingrs.append(ingr)
        print(len(ingrs))
        with open('conversion/' + path + '/nocup_ingr.json', 'w') as f:
            dic = {}
            dic['data'] = ingrs
            json.dump(dic, f)
        f.close()


def rename_cup_ingr_by_pairs(file, path):
    with open('conversion/' + file, 'r') as f:
        data = json.load(f)
    f.close()
    cup_ingrs = data['data']

    with open('conversion/cup_ingr_name_pairs.json', 'r') as f:
        mached_pairs = json.load(f)
    f.close()

    for ingr_meta in cup_ingrs:
        if ingr_meta[3] == 'cup':
            if ingr_meta[1] in mached_pairs.keys():
                ingr_name = ingr_meta[1]
                ingr_meta[-1] = mached_pairs[ingr_name]
                print(ingr_meta)

    with open('conversion/' + path + '/rename_cup_ingr_by_pairs.json', 'w') as f:
        data = {}
        data['data'] = cup_ingrs
        json.dump(data, f)
    f.close()

def volume2weight_by_chart(file, path):
    f_recipes = []
    with open('conversion/' + file, 'r') as f:
        raw_recipes = json.load(f)
    f.close()

    with open('conversion/first_step/ingr_conv_chart.json', 'r') as f:
        convert_table = json.load(f)
    f.close()

    amount = 0
    for recipe in raw_recipes['data']:
        print(recipe)
        ingr_name = recipe[-1]
        qty = float(recipe[2])
        if recipe[1] == '':
            del recipe
            continue
        if recipe[-2] == 'cup':
            print(ingr_name)
            m_score = 0
            m_ingr = {}
            for item_dic in convert_table:
                score = fuzz.token_set_ratio(ingr_name, item_dic['name'])
                if m_score < score:
                    m_score = score
                    m_ingr = item_dic
            if m_score > 45:
                print(m_ingr)
                if 'cup' in m_ingr['Volume']:
                    m_volu_info = m_ingr['Volume'].split(" ")
                    m_volu = m_volu_info[0]
                    m_qty = float(m_ingr['Gras'])
                    t_m_volu = fraction2decimal(m_volu)
                    t_m_qty = m_qty / t_m_volu
                    f_m_qty = t_m_qty * qty
                    recipe[2] = str(f_m_qty)
                    recipe[3] = 'gram'
                amount += 1
                f_recipes.append(recipe)
            else:
                f_recipes.append(recipe)
        else:
            f_recipes.append(recipe)

    with open('conversion/' + path + '/rename_cup_2weight.json', 'w') as f:
        data = {}
        data['data'] = f_recipes
        json.dump(data, f)
    f.close()
    print(amount)

def merge_cup_nocup(weighted_cupfile, nocupfile, path):
    with open('conversion/' + weighted_cupfile, 'r') as f:
        data = json.load(f)
    f.close()
    cup_ingr = data['data']

    with open('conversion/' + nocupfile, 'r') as f:
        data = json.load(f)
    f.close()
    no_cup_ingr = data['data']

    ingrs = no_cup_ingr + cup_ingr
    print(len(no_cup_ingr))
    print(len(cup_ingr))
    print(len(ingrs))

    with open("conversion/" + path + "/merged_nocup_weightedcup.json", "w") as f:
        data = {}
        data['data'] = ingrs
        json.dump(data,f)
    f.close()


def fifth_step():

    split2cupornocup(file='forth_step/new_corrected_meta.json', path='fifth_step', function='cup')
    split2cupornocup(file='forth_step/new_corrected_meta.json', path='fifth_step', function='nocup')
    rename_cup_ingr_by_pairs(file='fifth_step/cup_ingr.json', path='fifth_step')
    volume2weight_by_chart(file='fifth_step/rename_cup_ingr_by_pairs.json', path='fifth_step')
    merge_cup_nocup(weighted_cupfile='fifth_step/rename_cup_2weight.json', nocupfile='fifth_step/nocup_ingr.json', path='fifth_step')
    rename_missmapping_by_corrected(path='fifth_step', weird_file= 'forth_step/new_missmapped_meta.json', correct_file='fifth_step/merged_nocup_weightedcup.json' )
    mode_median_replace_solution(path='fifth_step', corect_file = 'fifth_step/merged_nocup_weightedcup.json', weird_file='fifth_step/rename_missmapped_weird_meta.json')


def main():
    forth_step()
    


if __name__ == '__main__':
    main()
