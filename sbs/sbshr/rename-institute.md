#### ``sbs_.infoInstitutes``

- **Alter** table:

```sql
ALTER TABLE `infoInstitutes`
	CHANGE COLUMN `name` `name` VARCHAR(60) NOT NULL AFTER `_LegacyID`,    -- ORIG: 45
	CHANGE COLUMN `fullname` `fullname` VARCHAR(80) NOT NULL AFTER `name`  -- ORIG: 60
;
```

- Do **update**!

```
UPDATE `infoInstitutes`
  SET `abbr`='IQB3',
  `name`='Quan ...',
  `fullname`='Institute of Quan ...'
  WHERE `id`=8;

```

----

#### ``_def_.js``

```bash
grep -ir "ISMB" . | less


# Then, search for: \./
```

- Was:

```js
{
  "abbr":"ISMB",
  "name":"Struc ..."
}
```

- Now:

```js
{
  "abbr":"IQB3",
  "name":"Quan ..."
}
```

----

#### ``personNames``

- Make a **backup**:

```sql
select pnID, institutePRIM
  from personNames
  where institutePRIM = 'ISMB'
;
```

- Do **update**!

```sql
UPDATE personNames
  SET institutePRIM = 'IQB3'
  WHERE institutePRIM = 'ISMB'
;
```


#### ``empRECs``

- Make a **backup**:

```sql
select empRecID, jsUniHR
  from empRECs
  where jsUniHR like '%ISMB%'
```

- Do **update**!

```sql
UPDATE empRECs                         -- !! empRECs
  SET
    _modifiedTime = _modifiedTime,
    jsUniHR = REPLACE(jsUniHR, 'ISMB', 'IQB3')
  WHERE
    jsUniHR like '%ISMB%'              -- !! jsUniHR
;
```


#### ``empRecSTARTERs``

_(Similarly...)_


- Make a **backup**:


```sql
select id, jsDATA
  from empRecSTARTERs
  where jsDATA like '%ISMB%'
```

- Do **update**!

```sql
UPDATE empRecSTARTERs                    -- !! empRecSTARTERs
  SET
    _modifiedTime = _modifiedTime,
    jsDATA = REPLACE( jsDATA, 'ISMB', 'IQB3')
  WHERE
    jsDATA like '%ISMB%'                 -- !! jsDATA
;
```


----


#### ``RECON`` script

- Change ``ISMB`` to ``IQB3``


#### ``UPDATE`` script

- Change ``ISMB`` to ``IQB3``
