package com.techmojo.roka;
import org.springframework.data.repository.CrudRepository;

import com.techmojo.roka.UserAccounts;

public interface AccountsRepository extends CrudRepository<UserAccounts, Long>{

}


// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

