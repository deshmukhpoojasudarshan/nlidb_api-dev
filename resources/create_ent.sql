
CREATE TABLE address (
	id UUID NOT NULL, 
	address_id VARCHAR(50), 
	address_1 VARCHAR(50), 
	address_2 VARCHAR(50), 
	address_3 VARCHAR(50), 
	postal_code VARCHAR(10), 
	country VARCHAR(50), 
	entry_user VARCHAR(50), 
	entry_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	modified_user VARCHAR(50), 
	modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	PRIMARY KEY (id)
)