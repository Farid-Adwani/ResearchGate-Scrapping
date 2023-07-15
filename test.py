from parsel import Selector

html = '''
<div class="nova-legacy-o-stack__item">
    <div class="nova-legacy-c-card nova-legacy-c-card--spacing-xl nova-legacy-c-card--elevation-1-above">
        <div class="nova-legacy-c-card__body nova-legacy-c-card__body--spacing-inherit">
            <div itemscope="" itemtype="http://schema.org/Person" class="nova-legacy-v-entity-item nova-legacy-v-entity-item--size-m">
                <div class="nova-legacy-v-entity-item__body">
                    <div class="nova-legacy-v-entity-item__stack nova-legacy-v-entity-item__stack--gutter-m">
                        <div class="nova-legacy-v-entity-item__stack-item">
                            <div class="nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-display nova-legacy-e-text--spacing-none nova-legacy-e-text--color-grey-900 nova-legacy-v-entity-item__title" itemprop="name">
                                <a class="nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare" href="profile/Jonathan-Arauz?_sg=XGsBL4z56eesBJGrk92g57BSIiljtMFU70CofyL5NuIW8BP4KNM99zWm4poX8cWf-M2cH5K6lhBNI2A">Jonathan Arauz</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

selector = Selector(text=html)
title = selector.css('.nova-legacy-v-entity-item__title a::text').get()

print(title)  # Output: Jonathan Arauz
