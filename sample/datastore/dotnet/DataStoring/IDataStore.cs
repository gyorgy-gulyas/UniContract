 
// <auto-generated>
//     This code was generated by unicontract
//     see more information: https://github.com/gyorgy-gulyas/UniContract
//
//     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
// </auto-generated>

using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using IConnection;using ICollection;
namespace DataStoring
{

	interface IDataStore
	{

		public IConnection Connection { get; }

		Task<bool> IsCollectionExists(string collectionName);
		Task<ICollection> GetCollectionByName(string collectionName);
		Task<ICollection> CreateCollection(string collectionName);
		Task<ICollection> DropCollection(ICollection collection);
	}

}