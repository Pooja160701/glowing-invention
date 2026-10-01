CREATE TABLE users (
  user_id VARCHAR PRIMARY KEY,
  signup_date DATE NOT NULL,
  platform VARCHAR(30),
  acquisition_source VARCHAR(100)
);

CREATE TABLE imports (
  import_id VARCHAR PRIMARY KEY,
  user_id VARCHAR NOT NULL,
  source_type VARCHAR(30) NOT NULL,
  status VARCHAR(30) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  completed_at TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE transactions (
  transaction_id VARCHAR PRIMARY KEY,
  user_id VARCHAR NOT NULL,
  import_id VARCHAR,
  transaction_date DATE NOT NULL,
  category VARCHAR(100),
  categorization_status VARCHAR(30),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE product_events (
  event_id VARCHAR PRIMARY KEY,
  user_id VARCHAR NOT NULL,
  event_name VARCHAR(100) NOT NULL,
  event_time TIMESTAMP NOT NULL,
  platform VARCHAR(30),
  product_version VARCHAR(30),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE experiment_assignments (
  experiment_id VARCHAR NOT NULL,
  user_id VARCHAR NOT NULL,
  variant VARCHAR(50) NOT NULL,
  assigned_at TIMESTAMP NOT NULL,
  PRIMARY KEY (experiment_id, user_id)
);
