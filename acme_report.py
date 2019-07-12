import random 
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved', 'Stinky', 'Huge']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Stick', 'Cheese', 'Mask']

def generate_products(num_products=30):
    products = []
    for num in range(num_products):
        adj= str(random.sample(ADJECTIVES, 1)).strip("['']")
        noun= str(random.sample(NOUNS, 1)).strip("['']")
        random_product= adj + ' ' + noun
        print(f'Generating Product: {random_product}')
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = round(random.uniform(0, 2.5), 2)
        products.append([random_product, price, weight, flammability])
    return products

def inventory_report(products):
    unique_products = 0
    for product in products:
        if product not in unique_products:
            unique_products += 1
    prices = [products[x][1] for x in range(len(products))]
    price_mean = round(sum(prices) / len(prices), 2)
    weights = [products[x][2] for x in range(len(products))]
    weights_mean = round(sum(weights) / len(weights), 2)
    flammabilites = [products[x][3] for x in range(len(products))]
    flammabilites_mean = round(sum(flammabilites) / len(flammabilites), 2)
    report= 'Unique Product Names: ' + str(unique_products) + '\nPrice mean: '+ str(price_mean) + '\nWeights mean: '+ str(weights_mean) + '\nFlammabilites mean: ' + str(flammabilites_mean)
    print(report)
    return 
   

if __name__ == '__main__':
    inventory_report(generate_products())