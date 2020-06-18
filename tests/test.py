from context import *

class Methods(unittest.TestCase):

    def test_merge_dicts(self):
        dicts = [{'a':[0,1,2], 'b':[], 'c':[]}, {'a':[0,3], 'b':[1]}]
        self.assertEqual(ppictx.merge_dicts(dicts), {'a': [0, 1, 2, 3], 'b': [1], 'c': []})

    def test_split_ids(self):
        self.assertEqual(ppictx.split_ids('pubmed:10938097'), ['10938097'])
        self.assertEqual(ppictx.split_ids('pubmed:14676191|pubmed:17979178|pubmed:26496610'), ['14676191', '17979178', '26496610'])

    def test_make_entry(self):
        entry = ppictx.make_entry(test='a', id=12, random=[1,2,3])
        self.assertIsInstance(entry, dict)
        self.assertEqual(entry, {'test': 'a', 'id': 12, 'random': [1, 2, 3]})

    def test_process_ppi(self):
        df = ppictx.process_ppi(fh)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(list(df.gene_a.values), ['FOXH1', 'PHF12', 'PARD3', 'JUND', 'IRAK1'])
        self.assertEqual(list(df.gene_b.values), ['FOXG1', 'HDAC1', 'YWHAH', 'BRCA1', 'MAPK8'])
        self.assertEqual(df.ids.values[0], 'pubmed:10938097|pubmed:20211142')
        self.assertEqual(df.ids.values[1], 'pubmed:11390640|pubmed:23752268|pubmed:26496610|pubmed:26841866|pubmed:28514442')
        self.assertEqual(df.ids.values[2], 'pubmed:14676191|pubmed:17979178|pubmed:26496610')
        self.assertEqual(df.ids.values[3], 'pubmed:12080089|pubmed:16713569')
        self.assertEqual(df.ids.values[4], '-')

    def test_process_pid_cla(self):
        data = ppictx.process_pid_cla(fp)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['20211142'], ['CVCL_6999', 'CVCL_0214'])
        self.assertEqual(data['23752268'], ['CVCL_0207', 'CVCL_0030', 'CVCL_0045'])
        self.assertEqual(data['28514442'], ['CVCL_0598', 'CVCL_0063', 'CVCL_0030', 'CVCL_0291', 'CVCL_5555'])
        self.assertEqual(data['26496610'], ['CVCL_1922'])

    def test_process_cla_cid(self):
        data = ppictx.process_cla_cid(fc)
        self.assertEqual(len(data), 10)
        self.assertEqual(data['CVCL_0207']['ID'], 'CCRF-CEM')
        self.assertEqual(data['CVCL_0214']['ID'], 'CHO-K1')
        self.assertEqual(data['CVCL_0045']['ID'], 'HEK293')
        self.assertEqual(data['CVCL_0045']['OX'], 'Homo sapiens')
        self.assertEqual(data['CVCL_0045']['SX'], 'Female')
        self.assertEqual(data['CVCL_0045']['CA'], 'Transformed cell line')

    def test_process_ppi_cid(self):
        data = ppictx.process_cla_cid(fc)
        self.assertEqual(len(data), 10)
        self.assertEqual(data['CVCL_0207']['ID'], 'CCRF-CEM')
        self.assertEqual(data['CVCL_0214']['ID'], 'CHO-K1')
        self.assertEqual(data['CVCL_0045']['ID'], 'HEK293')
        self.assertEqual(data['CVCL_0045']['OX'], 'Homo sapiens')
        self.assertEqual(data['CVCL_0045']['SX'], 'Female')
        self.assertEqual(data['CVCL_0045']['CA'], 'Transformed cell line')

    def test_process_ppi_cid(self):
        ppi = ppictx.process_ppi(fh)
        pid_cla = ppictx.process_pid_cla(fp)
        cla_cid = ppictx.process_cla_cid(fc)
        df, logs = ppictx.process_ppi_cid(ppi, pid_cla, cla_cid)

        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertIsInstance(logs, list)
        self.assertEqual(df.shape[0], 12)
        self.assertEqual(df.shape[1], 8)
        self.assertEqual(len(logs), 5)
        
        pids = [list(i.keys()) for i in logs]
        self.assertEqual(len(pids), 5)
        self.assertEqual(len([i for i in pids if len(i) > 0]), 4)
        self.assertEqual(len(set(itertools.chain.from_iterable(pids))), 11)

        clas = ppictx.merge_dicts(logs)
        self.assertEqual(len([k for k,v in clas.items() if len(v) == 0]), 7)
        self.assertEqual(len([k for k,v in clas.items() if len(v) > 0]), 4)
        self.assertEqual([len(v) for k,v in clas.items()], [0, 2, 0, 3, 1, 0, 5, 0, 0, 0, 0])

        valid = {row.gene_a+'_'+row.gene_b : ppictx.split_ids(row.ids) for i, row in ppi.iterrows()}
        # Expected interaction pairs
        self.assertTrue(all([a+'_'+b in valid.keys() for a,b in zip(df.gene_a.values, df.gene_b.values)]))
        # Expected matching of interaction pairs to pids
        self.assertTrue(all([pid in valid[a+'_'+b] for a,b,pid in zip(df.gene_a.values, df.gene_b.values, df.pid.values)]))
        # Expected matching of pids to cids
        self.assertTrue(all([cid in [cla_cid[cla]['ID'] for cla in pid_cla[pid]]
                             for pid,cid in zip(df.pid.values, df.cell_name.values)]))

    def test_process_raw_data(self):
        self.assertIsNone(ppictx.process_raw_data(fh, fp, fc))

if __name__ == '__main__':
    unittest.main()
