from django.test import TestCase

from indicadores_esus.indicator.models import (
    Indicator, IndicatorPattern, CalculatedIndicator
)
from indicadores_esus.core.utils import Quadrimester


class IndicatorTest(TestCase):

    def setUp(self):
        self.quad = Quadrimester(quad=1, year=2022)
        Indicator.objects.create(
            quadrimester=self.quad.abbrev,
            dt_init_evaluation=self.quad.evaluation_start,
            dt_end_evaluation=self.quad.evaluation_end,
        )
        Indicator.objects.create(
            quadrimester=self.quad.abbrev,
            dt_init_evaluation=self.quad.evaluation_start,
            dt_end_evaluation=self.quad.evaluation_end,
        )

    def test_only_one_indicator_is_active(self):
        ''' 
        Check if only one indicator related to one quadrimester is active
        '''
        indicators = Indicator.objects.filter(
            quadrimester=self.quad.abbrev, is_active=True
        )
        self.assertEqual(indicators.count(), 1)


class IndicatorPatternTest(TestCase):

    def setUp(self):
        IndicatorPattern.objects.create(
            type='1',
            parameter=100,
            goal=100,
            weight=1,
            year=2022,
        )
        IndicatorPattern.objects.create(
            type='1',
            parameter=100,
            goal=100,
            weight=1,
            year=2022,
        )

    def test_only_one_pattern_is_active(self):
        ''' 
        Check if only one indicator pattern related to one type and year is active
        '''
        patterns = IndicatorPattern.objects.filter(
            type='1', year=2022, is_active=True
        )
        self.assertEqual(patterns.count(), 1)    


class CalculatedIndicatorTest(TestCase):
    
    def setUp(self):
        quad = Quadrimester(quad=1, year=2022)
        self.base = Indicator.objects.create(
            quadrimester=quad.abbrev,
            dt_init_evaluation=quad.evaluation_start,
            dt_end_evaluation=quad.evaluation_end,
        )
        CalculatedIndicator.objects.create(
            numerator=0,
            denominator=0,
            indicator=self.base,
            indicator_index=0,
            type='1',
            status='2'
        )
        CalculatedIndicator.objects.create(
            numerator=0,
            denominator=0,
            indicator=self.base,
            indicator_index=0,
            type='1',
            status='1'
        )
        CalculatedIndicator.objects.create(
            numerator=0,
            denominator=0,
            indicator=self.base,
            indicator_index=0,
            type='2',
            status='1'
        )

    def test_only_one_indicator_is_generated_or_calculating(self):
        ''' 
        Check if only one calculated indicator related to one type and base 
        indicator has status generated or calculating
        '''
        indicators = CalculatedIndicator.objects.filter(
            type='1', indicator=self.base, status__in=['1', '2']
        )
        self.assertEqual(indicators.count(), 1)    
