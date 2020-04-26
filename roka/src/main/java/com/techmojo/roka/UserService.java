package com.techmojo.roka;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepository;
	
	@Autowired
	private AccountsRepository accountsRepository;
	
	public List<User> getAllUsers() {
		 	
		List<User> result = (List<User>) userRepository.findAll();
	         
	    if(result.size() > 0) {
	    	return result;
	            
	    } else {
	    	return new ArrayList<User>();
	    }
	}
	 
	public User getUserById(Long id) throws RecordNotFoundException {
		 
		Optional<User> employee = userRepository.findById(id);
		if(employee.isPresent()) {
			return employee.get();
	        } else {
	            throw new RecordNotFoundException("No employee record exist for given id");
	    }
	}
	 
	 public User createOrUpdateUser(User entity)  {
		 if(entity.getMobile()  == null) 
	        {
	            entity = userRepository.save(entity);
	             
	            return entity;
	        } 
	        else
	        {
	            Optional<User> employee = userRepository.findById(entity.getMobile());
	             
	            if(employee.isPresent()) 
	            {
	                User newEntity = employee.get();
	                newEntity.setMobile(entity.getMobile());
	                newEntity.setEmail(entity.getEmail());
	                newEntity.setName(entity.getName());
	                newEntity.setAddress(entity.getAddress());
	 
	                newEntity = userRepository.save(newEntity);
	                 
	                return newEntity;
	            } else {
	                entity = userRepository.save(entity);
	                return entity;
	            }
	        }
	    }
	  public void deleteUserById(Long id) throws RecordNotFoundException 
	    {
	        Optional<User> employee = userRepository.findById(id);
	         
	        if(employee.isPresent()) 
	        {
	            userRepository.deleteById(id);
	        } else {
	            throw new RecordNotFoundException("No employee record exist for given id");
	        }
	    }
}
