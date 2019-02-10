import pandas as pd

def no_targ_pop(df):
    df_new = df.drop('target_pop_flag', axis=1)
    new_Xy = [df_new.drop('recid_flag', axis=1),
              df_new['recid_flag']]
    return new_Xy

def no_years(df):
    df_new = df.drop(columns = [ 'year_released_2010',
                                      'year_released_2011',
                                      'year_released_2012',
                                      'year_released_2013',
                                      'year_released_2014',
                                      'year_released_2015',
                                      'reporting_year_2013',
                                      'reporting_year_2014',
                                      'reporting_year_2015',
                                      'reporting_year_2016',
                                      'reporting_year_2017',
                                      'reporting_year_2018'])

    new_Xy = [df_new.drop('recid_flag', axis=1),
                   df_new['recid_flag']]
    return new_Xy

def no_years_no_target(df):
    new_Xy = no_years(df)
    newXy = new_Xy[0].drop('target_pop_flag', axis=1), new_Xy[1]
    return newXy

def conv_subt(df):
    df_new = df[['recid_flag', 'target_pop_flag',
                       'year_released_2010',
                                   'year_released_2011',
                                      'year_released_2012',
                                      'year_released_2013',
                                      'year_released_2014',
                                      'year_released_2015',
                                      'reporting_year_2013',
                                      'reporting_year_2014',
                                      'reporting_year_2015',
                                      'reporting_year_2016',
                                      'reporting_year_2017',
                                      'reporting_year_2018',
                      'race_American Indian or Alaska Native - Non-Hispanic',
                      'race_Asian or Pacific Islander - Non-Hispanic',
                      'race_Black - Non-Hispanic',
                      'race_White - Hispanic',
                      'race_White - Non-Hispanic',
                      'age_at_release_25-34',
                      'age_at_release_35-44',
                      'age_at_release_45-54',
                      'age_at_release_55 and Older',
                      'age_at_release_Under 25',
                      'conviction_subtype_Alcohol',
                      'conviction_subtype_Animals',
                      'conviction_subtype_Arson',
                      'conviction_subtype_Assault',
                      'conviction_subtype_Burglary',
                      'conviction_subtype_Drug Possession',
                      'conviction_subtype_Flight/Escape',
                      'conviction_subtype_Forgery/Fraud',
                      'conviction_subtype_Kidnap',
                      'conviction_subtype_Murder/Manslaughter',
                      'conviction_subtype_OWI',
                      'conviction_subtype_Other Criminal',
                      'conviction_subtype_Other Drug',
                      'conviction_subtype_Other Public Order',
                      'conviction_subtype_Other Violent',
                      'conviction_subtype_Prostitution/Pimping',
                      'conviction_subtype_Robbery',
                      'conviction_subtype_Sex',
                      'conviction_subtype_Sex Offender Registry/Residency',
                      'conviction_subtype_Special Sentence Revocation',
                      'conviction_subtype_Stolen Property',
                      'conviction_subtype_Theft',
                      'conviction_subtype_Traffic',
                      'conviction_subtype_Trafficking',
                      'conviction_subtype_Vandalism',
                      'conviction_subtype_Weapons']]

    new_Xy = [df_new.drop('recid_flag', axis=1),df_new['recid_flag']]
    return new_Xy

def subt_no_target(df):
    new_Xy = conv_subt(df)
    newXy = [new_Xy[0].drop('target_pop_flag', axis=1), new_Xy[1]]
    return newXy

def subt_no_targ_no_years(df):
    new_Xy = subt_no_target(df)
    newXy = [new_Xy[0].drop(columns = [ 'year_released_2010',
                                      'year_released_2011',
                                      'year_released_2012',
                                      'year_released_2013',
                                      'year_released_2014',
                                      'year_released_2015',
                                      'reporting_year_2013',
                                      'reporting_year_2014',
                                      'reporting_year_2015',
                                      'reporting_year_2016',
                                      'reporting_year_2017',
                                      'reporting_year_2018']), new_Xy[1]]
    return newXy



def conv_class(df):
    df_new = df[['recid_flag', 'target_pop_flag',
                      'race_American Indian or Alaska Native - Non-Hispanic',
                      'race_Asian or Pacific Islander - Non-Hispanic',
                      'race_Black - Non-Hispanic',
                      'race_White - Hispanic',
                      'race_White - Non-Hispanic',
                      'age_at_release_25-34',
                      'age_at_release_35-44',
                      'age_at_release_45-54',
                      'age_at_release_55 and Older',
                      'age_at_release_Under 25',
                      'conviction_class_A Felony',
                      'conviction_class_Aggravated Misdemeanor',
                      'conviction_class_B Felony',
                      'conviction_class_C Felony',
                        'conviction_class_D Felony',
                        'conviction_class_Felony - Enhanced',
                        'conviction_class_Felony - Enhancement to Original Penalty',
                        'conviction_class_Felony - Mandatory Minimum',
                        'conviction_class_Other Felony',
                        'conviction_class_Other Felony (Old Code)',
                        'conviction_class_Serious Misdemeanor',
                        'conviction_class_Sexual Predator Community Supervision',
                        'conviction_class_Simple Misdemeanor',
                        'conviction_class_Special Sentence 2005']]  

    new_Xy = [df_new.drop('recid_flag', axis=1),df_new['recid_flag']]
    return new_Xy

def class_no_target(df):
    new_Xy = conv_class(df)
    newXy = new_Xy[0].drop('target_pop_flag', axis=1), new_Xy[1]
    return newXy


def conv_type(df):
    df_new = df[['recid_flag', 'target_pop_flag',
                      'race_American Indian or Alaska Native - Non-Hispanic',
                      'race_Asian or Pacific Islander - Non-Hispanic',
                      'race_Black - Non-Hispanic',
                      'race_White - Hispanic',
                      'race_White - Non-Hispanic',
                      'age_at_release_25-34',
                      'age_at_release_35-44',
                      'age_at_release_45-54',
                      'age_at_release_55 and Older',
                      'age_at_release_Under 25',
                      'convicting_type_Drug',
                      'convicting_type_Other',
                      'convicting_type_Property',
                      'convicting_type_Public Order',
                      'convicting_type_Violent']]  

    new_Xy = [df_new.drop('recid_flag', axis=1),df_new['recid_flag']]
    return new_Xy

def type_no_target(df):
    new_Xy = conv_type(df)
    newXy = new_Xy[0].drop('target_pop_flag', axis=1), new_Xy[1]
    return newXy
