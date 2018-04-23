# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UfcFighterItem(scrapy.Item):
    # define the fields for your item here like:
    image = scrapy.Field()
    name = scrapy.Field()
    quote = scrapy.Field()
    url = scrapy.Field()
    fighter_age = scrapy.Field()
    fighter_college = scrapy.Field()
    fighter_degree = scrapy.Field()
    fighter_from = scrapy.Field()
    fighter_height = scrapy.Field()
    fighter_nickname = scrapy.Field()
    fighter_lives_in = scrapy.Field()
    fighter_leg_reach = scrapy.Field()
    fighter_reach = scrapy.Field()
    fighter_skill_record = scrapy.Field()
    fighter_skill_summary = scrapy.Field()
    fighter_weight = scrapy.Field()
