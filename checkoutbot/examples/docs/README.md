# Checkout Bot Examples

This directory contains examples to help you get started with the Checkout Bot framework/library.

## Structure

- `config/`: Contains example configuration files.
- `scripts/`: Contains example scripts to run the bot using the configurations.
- `docs/`: Contains documentation for the examples.

## How to Use

1. **Example Configuration**:

   - `example_config.json`: A sample configuration file for setting up the bot. Modify this file with your details.
   - `example_template1.json` and `example_template2.json`: Sample templates to load predefined configurations.

2. **Example Scripts**:
   - `run_example_config.py`: Script to run the bot using `example_config.json`.
   - `run_template1.py` and `run_template2.py`: Scripts to run the bot using `example_template1.json` and `example_template2.json`.

## Running the Examples

1. Ensure you have all dependencies installed and the `checkoutbot` package is available.
2. Modify the configuration files in the `config` directory to match your use case.
3. Run the example scripts from the `scripts` directory:

   ```sh
   python examples/scripts/run_example_config.py
   python examples/scripts/run_template1.py
   python examples/scripts/run_template2.py
   ```

## Configuration Details

### General Settings

- `enable_proxy`: Boolean value to enable or disable proxy usage.
- `proxies`: List of proxy URLs if `enable_proxy` is set to true.
- `enable_ai`: Boolean value to enable or disable AI simulation.

### Payment Settings

- `payment_method`: Either `credit-card` or `paypal`.
- `card_name`, `card_number`, `expiry_date`, `cvv`, `billing_address`: Details for credit card payment.
- `paypal_client_id`, `paypal_client_secret`: Details for PayPal payment.

### Scraping Settings

- `search_method`: Either `url` or `name`.
- `product_url`: Direct URL of the product if `search_method` is `url`.
- `website_url`, `product_name`: Details for searching by product name.
- `min_price`, `max_price`: Price range for the product.
- `quantity`: Number of items to scrape.
- `start_date`, `start_time`: When to start scraping.
- `duration`: Duration of scraping in minutes.
- `frequency`: Frequency of scraping in seconds.

For more details, refer to the `config/example_config.json` and `config/example_template1.json` files.
